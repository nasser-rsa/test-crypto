# Ejecución de la aplicación y pruebas

## Configuración

Para poder ejecutar la aplicación, es necesario seguir los siguientes pasos:

1. Descargar e instalar Python (en mi caso 3.10).
2. Abrir una terminal y clonar el repositorio usando el comando git clone `https://github.com/nasser-rsa/test-crypto.git` o descargar el archivo directamente desde el repositorio.
3. Navegar hasta el directorio `test-crypto` ejecutando el siguiente comando en la terminal:

```bash
cd test-crypto
```
4. Crear un entorno virtual ejecutando el siguiente comando en la terminal:

```bash
python3.10 -m venv venv
```

Esto creará una carpeta llamada `venv` que contendrá el entorno virtual.
5. Activa el entorno virtual con el siguiente comando:

```bash
source venv/bin/activate
```

Si estás utilizando Windows, el comando para activar el entorno virtual es diferente. Deberás utilizar el siguiente comando en la terminal:

```bash
venv\Scripts\activate
```

6. Instalar las librerías necesarias mediante el archivo `requirements.txt` ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Pruebas

Para ejecutar las pruebas unitarias de la aplicación, es necesario abrir una terminal en la ubicación del archivo `requirements.txt` y escribir el siguiente comando:

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
