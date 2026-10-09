# Utilizamos una imagen liviana que ya contiene Python 3.13.
FROM python:3.13-slim
# Creamos y seleccionamos /app como carpeta de trabajo
# dentro del contenedor.
WORKDIR /app
# Copiamos primero el archivo con las dependencias.
COPY requirements.txt .
# Instalamos las librerías necesarias para ejecutar la API.
# --no-cache-dir evita guardar archivos temporales de instalación.
RUN pip install --no-cache-dir -r requirements.txt
# Copiamos la carpeta de nuestra aplicación al contenedor.
COPY app ./app
# Documentamos que la API utiliza el puerto 8000.
EXPOSE 8000
# Comando que se ejecutará cuando arranque el contenedor.
# --host 0.0.0.0 permite acceder a la API desde fuera del contenedor.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]