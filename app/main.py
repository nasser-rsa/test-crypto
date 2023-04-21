from flask import Flask, jsonify
import requests
import json
import sqlite3
import pandas as pd

app = Flask(__name__)

def create_database():
    """ Create a SQLite database and three tables if they don't already exist. """

    with sqlite3.connect('data.db') as conn:
        c = conn.cursor()

        try:
            c.execute('''CREATE TABLE IF NOT EXISTS symbols
                         (id INTEGER PRIMARY KEY,
                         symbol TEXT)''')

            c.execute('''CREATE TABLE IF NOT EXISTS bids
                         (id INTEGER PRIMARY KEY,
                         symbol_id INTEGER,
                         price FLOAT,
                         quantity FLOAT,
                         FOREIGN KEY (symbol_id) REFERENCES symbols(id))''')

            c.execute('''CREATE TABLE IF NOT EXISTS asks
                         (id INTEGER PRIMARY KEY,
                         symbol_id INTEGER,
                         price FLOAT,
                         quantity FLOAT,
                         FOREIGN KEY (symbol_id) REFERENCES symbols(id))''')

            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            conn.rollback()

def load_data(symbol):
    """ Fetches the order book data for a given symbol from the Blockchain.com API and stores it in a SQLite database. """

    url = f"https://api.blockchain.com/v3/exchange/l3/{symbol}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error {response.status_code} fetching data for symbol {symbol}")
    data = json.loads(response.text)

    # Insert symbol into symbols table and retrieve ID
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        symbol_id = cursor.execute("INSERT OR IGNORE INTO symbols (symbol) VALUES (?)", (symbol,)).lastrowid

        # Insert bids into bids table
        bids = []
        for bid in data['bids']:
            price = bid['px']
            quantity = bid['qty']
            bids.append((symbol_id, price, quantity))
        cursor.executemany("INSERT INTO bids (symbol_id, price, quantity) VALUES (?, ?, ?)", bids)

        # Insert asks into asks table
        asks = []
        for ask in data['asks']:
            price = ask['px']
            quantity = ask['qty']
            asks.append((symbol_id, price, quantity))
        cursor.executemany("INSERT INTO asks (symbol_id, price, quantity) VALUES (?, ?, ?)", asks)

        conn.commit()


def get_order_book_data_from_db(side):
    """ Retrieves order book data from a SQLite database for a given side. """

    query = """
    SELECT symbols.symbol, {0}.id, {0}.price, {0}.quantity 
    FROM {0} JOIN symbols ON {0}.symbol_id=symbols.id
    """.format(side)

    with sqlite3.connect('data.db') as conn:
        df = pd.read_sql_query(query, conn)

    average_value = df['price'].mean()
    greater_value = df.loc[df['price'] == df['price'].max(), ['price', 'quantity', 'id']]
    lesser_value = df.loc[df['price'] == df['price'].min(), ['price', 'quantity', 'id']]
    total_qty = df['quantity'].sum()
    total_px = (df['price'] * df['quantity']).sum()

    output_dict = {
        f'{side}': {
            'average_value': average_value,
            'greater_value': {
                'px': greater_value['price'].iloc[0],
                'qty': greater_value['quantity'].iloc[0],
                'num': int(greater_value['id'].iloc[0]),
                'value': greater_value['price'].iloc[0] * greater_value['quantity'].iloc[0]
            },
            'lesser_value': {
                'px': lesser_value['price'].iloc[0],
                'qty': lesser_value['quantity'].iloc[0],
                'num': int(lesser_value['id'].iloc[0]),
                'value': lesser_value['price'].iloc[0] * lesser_value['quantity'].iloc[0]
            },
            'total_qty': total_qty,
            'total_px': total_px
        }
    }
    return output_dict

def get_general_statistics(symbol):
    """ Retrieves and computes general statistics for bids and asks data of a given symbol from a SQLite database. """

    bids_query = 'SELECT price, quantity FROM bids JOIN symbols ON bids.symbol_id=symbols.id WHERE symbols.symbol=?'
    asks_query = 'SELECT price, quantity FROM asks JOIN symbols ON asks.symbol_id=symbols.id WHERE symbols.symbol=?'

    with sqlite3.connect('data.db') as conn:
        # Retrieve bids and asks data from the database
        bids_df = pd.read_sql_query(bids_query, conn, params=[symbol])
        asks_df = pd.read_sql_query(asks_query, conn, params=[symbol])

    bids_qty = bids_df['quantity'].sum()
    bids_value = (bids_df['price'] * bids_df['quantity']).sum()
    asks_qty = asks_df['quantity'].sum()
    asks_value = (asks_df['price'] * asks_df['quantity']).sum()


    output_dict = {
        f'{symbol}': {
            'bids': {
                'count': len(bids_df),
                'qty': bids_qty,
                'value': bids_value
            },
            'asks': {
                'count': len(asks_df),
                'qty': asks_qty,
                'value': asks_value
            }
        }
    }
    return output_dict

@app.route('/bids')
def get_bids_route():
    """ Returns the bid data from the order book. """
    return get_order_book_data_from_db('bids')

@app.route('/asks')
def get_asks_route():
    """ Returns the ask data from the order book. """
    return get_order_book_data_from_db('asks')

@app.route('/general_statistics/<symbol>')
def get_general_statistics_route(symbol):
    """ Get general statistics for a given symbol. """
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT id FROM symbols WHERE symbol=?", (symbol,))
    symbol_id = c.fetchone()
    conn.close()

    if symbol_id is None:
        load_data(symbol)

    output_dict = get_general_statistics(symbol)
    return output_dict

if __name__ == '__main__':
    symbol = input("Enter a symbol like 'BTC-USD': ")
    create_database()
    load_data(symbol)
    app.run()