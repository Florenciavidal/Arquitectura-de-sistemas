# Imagen base liviana de Python
FROM python:3.13.3-slim

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código Python al contenedor
COPY main.py /app/
# COPY tasks.json /app/  ← opcional si tienes uno pre-creado

# Comando por defecto para ejecutar
CMD ["python", "main.py"]
