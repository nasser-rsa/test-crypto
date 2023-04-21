# Ejecución de la aplicación y pruebas

## Configuración

Para poder ejecutar la aplicación, es necesario seguir los siguientes pasos:

1. Descargar e instalar Python (versión 3.8 o superior).
2. Clonar el repositorio que contiene el archivo `main.py` usando el comando git clone `https://github.com/nasser-rsa/test-crypto.git` en la línea de comandos o descargar el archivo directamente desde el repositorio.
3. Instalar las librerías necesarias utilizando el archivo `requirements.txt` mediante el comando `pip install -r requirements.txt`.

## Pruebas

Para ejecutar las pruebas unitarias de la aplicación, es necesario abrir una terminal en la ubicación del archivo `main.py` y escribir el siguiente comando:

```bash
python -m unittest discover
```

Este comando ejecutará todas las pruebas unitarias de la aplicación y mostrará el resultado en la terminal. Si todas las pruebas pasan correctamente, se mostrará un mensaje de éxito. En caso contrario, se mostrarán los errores correspondientes.

## Ejecución

Para ejecutar la aplicación, es necesario abrir una terminal en la ubicación del archivo `main.py` y escribir el siguiente comando:

```bash
cd app
python main.py
```

Este comando iniciará el servidor y la aplicación estará disponible en la siguiente dirección: http://127.0.0.1:5000/.

Tiene tres endpoint `/bids`, `/asks` y `/general_statistics` para mostrar los datos de la tabla de la base de datos SQLite. Estos datos se cargan utilizando la API de Blockchain.com.