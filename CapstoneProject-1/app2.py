from flask import Flask, jsonify, request
import time
import random
import logging

app = Flask(__name__)

# -----------------------------
# Logging (Observability)
# -----------------------------
logging.basicConfig(level=logging.INFO)

# -----------------------------
# In-Memory DB (Demo purpose)
# -----------------------------
products = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Phone", "price": 30000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

cart = []

# -----------------------------
# Root Endpoint
# -----------------------------
@app.route("/")
def home():
    return jsonify({"message": "E-Commerce Microservice Running 🚀"}), 200


# -----------------------------
# Health Check (K8s Probes)
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/ready", methods=["GET"])
def readiness():
    return jsonify({"status": "READY"}), 200


# -----------------------------
# Product Service
# -----------------------------
@app.route("/products", methods=["GET"])
def get_products():
    logging.info("Fetching all products")
    return jsonify(products), 200


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404


# -----------------------------
# Cart Service
# -----------------------------
@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(cart), 200


@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json(silent=True) or {}
    product_id = data.get("product_id")

    if not product_id:
        return jsonify({"error": "product_id is required"}), 400

    for product in products:
        if product["id"] == product_id:
            cart.append(product)
            logging.info(f"Added product {product_id} to cart")
            return jsonify({"message": "Added to cart"}), 201

    return jsonify({"error": "Product not found"}), 404


# -----------------------------
# Checkout Service (Simulated)
# -----------------------------
@app.route("/checkout", methods=["POST"])
def checkout():
    logging.info("Processing checkout...")

    if not cart:
        return jsonify({"error": "Cart is empty"}), 400

    # Simulate latency (real-world issue)
    delay = random.randint(1, 5)
    time.sleep(delay)

    # Simulate failure scenario (30% chance)
    if random.random() < 0.3:
        logging.error("Payment service failed!")
        return jsonify({
            "status": "FAILED",
            "reason": "Payment gateway error"
        }), 500

    cart.clear()
    return jsonify({
        "status": "SUCCESS",
        "message": "Order placed successfully"
    }), 200
# -----------------------------
# Metrics Endpoint (Basic)
# -----------------------------
@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify({
        "total_products": len(products),
        "cart_items": len(cart)
    }), 200


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
