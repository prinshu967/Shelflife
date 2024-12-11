from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize MongoDB
mongo = PyMongo()
# print(f"Loaded MONGO_URI: {os.getenv('MONGO_URI')}")  

def create_app():
    app = Flask(__name__)

    # Configure app with environment variables
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Check if the MONGO_URI is None
    if app.config['MONGO_URI'] is None:
        # print("MONGO_URI is missing in the environment variables!")
        raise ValueError("MONGO_URI is not defined in the environment")

    # Initialize MongoDB with the app inside a try-except block
    try:
        mongo.init_app(app)
        print("MongoDB connection initialized successfully!")
    except Exception as e:
        print(f"Error initializing MongoDB: {e}")
        raise e  # Re-raise the exception to halt the app initialization

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
