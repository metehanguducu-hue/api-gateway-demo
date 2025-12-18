from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

if __name__ == "__main__":
    app.run(port=5001)
