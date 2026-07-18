from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"status": "pong"})

@app.route("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/echo", methods=["POST"])
def echo():
    payload = request.json or {}
    return jsonify({"you_sent": payload})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
