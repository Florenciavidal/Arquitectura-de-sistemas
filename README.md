# 🗂️ EmpraTasks — Sistema de Gestión de Tareas Distribuido

**EmpraTasks** es una aplicación web desarrollada como parte del curso **TICS317 - Arquitectura de Sistemas**. Su objetivo es demostrar el uso de múltiples servidores con balanceo de carga para distribuir solicitudes de manera eficiente, simulando el funcionamiento de sistemas web reales a gran escala.

---

## 🚀 Características

- 🧠 Servidores Flask independientes (puerto 5001 y 5002).
- 📦 Balanceador de carga en Flask (puerto 8080).
- ✅ Gestión de tareas: agregar, completar, eliminar.
- 🧊 Interfaz moderna, profesional y responsive.
- 📅 Visualización de fecha y puerto activo.
- 💾 Persistencia local con `tasks.json`.

---

## 🏗️ Estructura del Proyecto

Arquitectura-de-sistemas/
├── app.py # Servidor Flask para tareas
├── load_balancer.py # Balanceador de carga
├── tasks.json # Almacén local de tareas
├── venv/ # Entorno virtual 
└── templates/
└── index.html # Interfaz visual de la app

---

## ⚙️ Requisitos

- Python 3.7 o superior
- pip
- Entorno virtual recomendado (`venv`)

Instalación de dependencias:
```bash
pip install flask requests
