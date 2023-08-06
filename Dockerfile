# Establecer la imagen base
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos a la imagen
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que se ejecuta la aplicación
EXPOSE 5000

# Iniciar la aplicación
CMD ["python", "app.py"]
