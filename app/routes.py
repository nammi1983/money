from flask import render_template, request, jsonify
from app import app
from app.models import train_reinforcement_learning_model
from app.utils import enforce_policies, plot_stock_data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train", methods=["POST"])
def train():
    try:
        model = train_reinforcement_learning_model()
        return jsonify({"message": "Model trained successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        if not data or "feature1" not in data or "feature2" not in data:
            return jsonify({"error": "Invalid input data"}), 400

        feature1 = float(data["feature1"])
        feature2 = float(data["feature2"])
        prediction = enforce_policies(feature1 + feature2)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/plot", methods=["POST"])
def plot():
    try:
        data = request.json
        if not data or "symbol" not in data:
            return jsonify({"error": "Invalid input data"}), 400

        symbol = data["symbol"]
        dates, prices = plot_stock_data(symbol)  # Fetch and return data
        return jsonify({"dates": dates, "prices": prices})
    except Exception as e:
        return jsonify({"error": str(e)}), 500