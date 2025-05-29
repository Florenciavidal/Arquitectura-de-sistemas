from flask import Flask, request, Response
import requests, random

app = Flask(__name__)

SERVERS = ['http://localhost:5001', 'http://localhost:5002']

@app.route('/', defaults={'path': ''}, methods=["GET", "POST"])
@app.route('/<path:path>', methods=["GET", "POST"])
def proxy(path):
    target = random.choice(SERVERS)
    url = f"{target}/{path}"
    method = request.method

    try:
        if method == "POST":
            resp = requests.post(url, data=request.form)
        else:
            resp = requests.get(url)
        return Response(resp.content, resp.status_code, resp.headers.items())
    except requests.exceptions.ConnectionError:
        return f"Servidor {target} no disponible", 503

if __name__ == '__main__':
    app.run(port=8080)
