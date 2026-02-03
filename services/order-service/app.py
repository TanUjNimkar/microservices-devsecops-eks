from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP", service="order-service")

@app.route("/orders")
def orders():
    return jsonify(orders=["order-101", "order-102"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
