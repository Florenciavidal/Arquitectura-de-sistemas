from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

servers = ["http://localhost:5001", "http://localhost:5002"]
current = 0

@app.route('/<path:path>', methods=['GET', 'POST'])
def balancear(path):
    global current
    destino = servers[current]
    current = (current + 1) % len(servers)
    url = f"{destino}/{path}"
    try:
        if request.method == 'POST':
            resp = requests.post(url, json=request.get_json())
        else:
            resp = requests.get(url)
        return resp.text, resp.status_code
    except Exception:
        return "Servidor no disponible", 502

@app.route('/status')
def status():
    return jsonify({"balanceador": "activo"})

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(port=8080)
