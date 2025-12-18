from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def orders():
    return jsonify({"orders": ["Order-1", "Order-2"]})

if __name__ == "__main__":
    app.run(port=5002)
