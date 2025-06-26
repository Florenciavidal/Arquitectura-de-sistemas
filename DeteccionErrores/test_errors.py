import requests

base_url = "http://localhost:8080"

# 400 - JSON vacío
requests.post(f"{base_url}/tarea")

# 404 - ruta inexistente
requests.get(f"{base_url}/no_existe")

# 500 - error interno intencional
requests.get(f"{base_url}/causar500")

# Mostrar estadísticas
resp = requests.get(f"{base_url}/errors/stats")
data = resp.json()
print("Total errores:", data["total_errors"])
print("Tipos de errores:", data["error_types"])
print("Errores recientes:", data["recent_errors"])
