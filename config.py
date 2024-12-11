import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Provide a default value for development
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/default_db')  # Provide a default local URI
