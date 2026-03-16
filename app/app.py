from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return {
        "message": "Multi-tenant website running",
        "pod": hostname
    }

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)