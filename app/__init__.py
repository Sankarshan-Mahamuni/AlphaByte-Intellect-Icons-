from flask import Flask

# Initialize the Flask application
app = Flask()

# Set up a secret key for session management (replace 'your_secret_key' with a random string)
app.secret_key = 'your_secret_key'

# Import the routes module to register the routes with the Flask app
from app import routes