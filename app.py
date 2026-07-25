from flask import Flask, request, jsonify

app = Flask(__name__)

dax = {
    "price": 0
}

@app.route("/")
def home():
    return f"DAX: {dax['price']}"

@app.route("/api/dax")
def get_dax():
    return jsonify(dax)

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()

    if "price" in data:
        dax["price"] = data["price"]

    return "OK"
