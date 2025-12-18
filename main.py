from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "12345"

@app.before_request
def check_api_key():
    if request.headers.get("X-API-KEY") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@app.route("/users")
def users():
    response = requests.get("http://localhost:5001/users")
    return response.json()

@app.route("/orders")
def orders():
    response = requests.get("http://localhost:5002/orders")
    return response.json()

if __name__ == "__main__":
    app.run(port=5000)
