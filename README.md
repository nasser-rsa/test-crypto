# Ejecución de la aplicación y pruebas

## Configuración

Para poder ejecutar la aplicación, es necesario seguir los siguientes pasos:

1. Descargar e instalar Python (versión 3.8 o superior).
2. Abrir una terminal y clonar el repositorio usando el comando git clone `https://github.com/nasser-rsa/test-crypto.git` o descargar el archivo directamente desde el repositorio.
3. Navegar hasta el directorio `test-crypto`

```bash
cd test-crypto
```
4. Crea un entorno virtual con el siguiente comando:

```bash
python -m venv venv
```

Este comando creará una carpeta llamada venv que contendrá el entorno virtual.

5. Activa el entorno virtual con el siguiente comando:

```bash
source venv/bin/activate
```

Si usas Windows, el comando para activar el entorno virtual es diferente. Debes usar el siguiente comando:

```bash
venv\Scripts\activate
```

6. Instalar las librerías necesarias utilizando el archivo `requirements.txt` mediante el siguiente comando

```bash
pip install -r requirements.txt
```

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
