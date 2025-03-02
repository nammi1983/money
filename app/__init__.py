from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Import routes and other components
from app import routes