from flask import Flask, request, jsonify
import sys
import json
import os

app = Flask(__name__)

LOG_FILE = "error_log.json"

# Cargar historial desde JSON si existe
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        data = json.load(f)
        error_log = data.get("log", [])
        error_stats = data.get("stats", {
            "400_BAD_REQUEST": 0,
            "404_NOT_FOUND": 0,
            "500_INTERNAL_ERROR": 0
        })
else:
    error_log = []
    error_stats = {
        "400_BAD_REQUEST": 0,
        "404_NOT_FOUND": 0,
        "500_INTERNAL_ERROR": 0
    }

# Guardar errores en archivo
def guardar_log():
    with open(LOG_FILE, "w") as f:
        json.dump({
            "log": error_log,
            "stats": error_stats
        }, f, indent=2)

@app.route('/tarea', methods=['POST'])
def crear_tarea():
    data = request.get_json()
    if not data:
        error_stats["400_BAD_REQUEST"] += 1
        error_log.append("400 - JSON vacío o malformado")
        guardar_log()
        return "JSON inválido", 400
    return "Tarea recibida", 200

@app.route('/causar500')
def causar_error():
    try:
        1 / 0
    except Exception:
        error_stats["500_INTERNAL_ERROR"] += 1
        error_log.append("500 - Error interno de servidor")
        guardar_log()
        return "Error interno", 500

@app.route('/errors/stats')
def error_stats_view():
    return jsonify({
        'total_errors': sum(error_stats.values()),
        'error_types': error_stats,
        'recent_errors': error_log[-10:]
    })

@app.errorhandler(404)
def not_found(e):
    error_stats["404_NOT_FOUND"] += 1
    error_log.append("404 - Recurso no encontrado")
    guardar_log()
    return "Recurso no encontrado", 404

if __name__ == '__main__':
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    app.run(port=puerto)
