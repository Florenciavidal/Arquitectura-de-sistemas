# (DOCKER) Task Manager - Arquitectura de Sistemas (TICS317)

Este es un proyecto simple de consola hecho en Python y Docker, que permite gestionar tareas almacenadas en un archivo `tasks.json`. Fue desarrollado como parte del curso **Arquitectura de Sistemas (TICS317)**, para practicar conceptos como:

- Manejo de archivos
- Tipado estático
- Contenedores con Docker
- Separación de lógica y persistencia

---

## 🐳 Ejecutar con Docker

### 1. Construir la imagen

Desde la terminal, ubicado en la carpeta del proyecto:

docker build -t task-manager .

## 2. Ejecutar el contenedor de forma interactiva

docker run -it -v "$(pwd)":/app task-manager

El uso de -v "$(pwd)":/app permite montar el volumen local, para que los cambios en tasks.json se guarden fuera del contenedor.

### 📂 Estructura del proyecto


Monolitico/
├── main.py         # Código fuente principal
├── tasks.json      # Archivo de almacenamiento de tareas
└── Dockerfile      # Instrucciones para construir la imagen Docker
🧪 ¿Cómo funciona?

Carga las tareas desde tasks.json (o crea una lista vacía si no existe).
Muestra las tareas actuales por consola.
Pide una nueva tarea al usuario.
Guarda el resultado actualizado en tasks.json.

### Requisitos

Docker Desktop instalado y en ejecución
Python 3.13 (dentro del contenedor)
Terminal con acceso a comandos Docker

### Compartir imagen

Puedes exportar e importar la imagen en otro equipo:

# Guardar la imagen como archivo .tar

docker save -o task-manager.tar task-manager

# En otro equipo, importar la imagen
d
ocker load -i task-manager.tar
