import os
from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.models import train_reinforcement_learning_model
from app.utils import (
    enforce_policies, 
    plot_stock_data, 
    auto_invest, 
    automate_freelance_work, 
    manage_affiliate_marketing, 
    optimize_ecommerce, 
    adaptive_ai_trading, 
    self_learning_ai, 
    auto_error_fix, 
    detect_fraud, 
    recognize_voice, 
    recognize_face
)

# Initialize the Flask app and set the template folder to E:\money\templates
app = Flask(__name__, template_folder=r"E:\money\templates")

# Set secret key for CSRF protection
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default-secret-key")

# Enable CSRF protection
csrf = CSRFProtect(app)

# Define a custom Content Security Policy to allow external links for our dropdowns
csp = {
    'default-src': [
        '\'self\'',
        'https://www.robinhood.com',
        'https://www.etrade.com',
        'https://www.tdameritrade.com',
        'https://www.fiverr.com',
        'https://www.upwork.com',
        'https://www.freelancer.com',
        'https://affiliate-program.amazon.com',
        'https://www.clickbank.com',
        'https://www.cj.com',
        'https://www.shopify.com',
        'https://www.bigcommerce.com',
        'https://woocommerce.com',
        'https://www.etoro.com',
        'https://www.interactivebrokers.com'
    ]
}

# Add security headers using Talisman with custom CSP (disable HTTPS for development)
Talisman(app, force_https=False, content_security_policy=csp)

# Enable rate limiting
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

# Define the home route that serves index.html from E:\money\templates
@app.route("/")
def home():
    return render_template("index.html")

# Define fraud detection route
@app.route("/detect-fraud", methods=["POST"])
@limiter.limit("10 per minute")
def fraud_detection_route():
    try:
        data = request.json
        result = detect_fraud(data)
        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define voice recognition route
@app.route("/recognize-voice", methods=["POST"])
@limiter.limit("10 per minute")
def voice_recognition_route():
    try:
        audio_data = request.files["audio"]
        result = recognize_voice(audio_data)
        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define face recognition route
@app.route("/recognize-face", methods=["POST"])
@limiter.limit("10 per minute")
def face_recognition_route():
    try:
        image_data = request.files["image"]
        result = recognize_face(image_data)
        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use environment PORT or default to 8000
    app.run(host="0.0.0.0", port=port, debug=False)  # Production mode
