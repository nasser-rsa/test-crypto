import sqlite3
import unittest
from unittest.mock import patch
from app import app, create_database, load_data, get_order_book_data_from_db, get_general_statistics

class TestApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create a test database and load test data into it
        create_database()
        load_data('BTC-USD')
    
    @classmethod
    def tearDownClass(cls):
        # Drop the test tables from the test database
        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute('DROP TABLE IF EXISTS symbols')
            c.execute('DROP TABLE IF EXISTS bids')
            c.execute('DROP TABLE IF EXISTS asks')
            conn.commit()

    
    def test_get_bids_route(self):
        with app.test_client() as client:
            response = client.get('/bids')
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertIn('bids', data)
            self.assertIn('average_value', data['bids'])
            self.assertIn('greater_value', data['bids'])
            self.assertIn('lesser_value', data['bids'])
            self.assertIn('total_qty', data['bids'])
            self.assertIn('total_px', data['bids'])
    
    def test_get_order_book_data_from_db(self):
        data = get_order_book_data_from_db('bids')
        self.assertIn('bids', data)
        self.assertIn('average_value', data['bids'])
        self.assertIn('greater_value', data['bids'])
        self.assertIn('lesser_value', data['bids'])
        self.assertIn('total_qty', data['bids'])
        self.assertIn('total_px', data['bids'])
    
    def test_get_general_statistics(self):
        data = get_general_statistics('BTC-USD')
        self.assertIn('BTC-USD', data)
        self.assertIn('bids', data['BTC-USD'])
        self.assertIn('asks', data['BTC-USD'])
        self.assertIn('count', data['BTC-USD']['bids'])
        self.assertIn('qty', data['BTC-USD']['bids'])
        self.assertIn('value', data['BTC-USD']['bids'])
        self.assertIn('count', data['BTC-USD']['asks'])
        self.assertIn('qty', data['BTC-USD']['asks'])
        self.assertIn('value', data['BTC-USD']['asks'])
