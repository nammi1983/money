import os
from flask import Flask, render_template, request, jsonify
from app.models import train_reinforcement_learning_model
from app.utils import enforce_policies, plot_stock_data

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return render_template("index.html")

# Define the train route
@app.route("/train", methods=["POST"])
def train():
    try:
        model = train_reinforcement_learning_model()
        return jsonify({"message": "Model trained successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define the predict route
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

# Define the plot route
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

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Render's PORT or default to 8000
    app.run(host="0.0.0.0", port=port)