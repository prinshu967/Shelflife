from flask import Blueprint, request, jsonify, render_template
from datetime import datetime
import os
from .helpers import predict_shelf_life
from .models import predict_image
from . import mongo
from PIL import Image
import io

# Allowed image extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'bmp', 'gif'}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Blueprint definition
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@main.route('/predict', methods=['POST'])
def predict():
    """
    Handle file uploads and predict the shelf life of the uploaded fruit or vegetable image.
    """
    try:
        # Ensure a file is provided
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files['file']
        if not file:
            return jsonify({"error": "No file provided"}), 400

        # Check if the file has an allowed image extension
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type. Allowed types are: jpg, jpeg, png, bmp, gif."}), 400

        # Read the file directly into memory as a PIL image
        try:
            image = Image.open(file.stream)
        except Exception as img_error:
            return jsonify({"error": "Invalid image file", "details": str(img_error)}), 400

        # Convert the image to RGB if it has an alpha channel (RGBA)
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Convert the image into a byte stream to simulate file input
        byte_io = io.BytesIO()
        image.save(byte_io, format='JPEG')  # Save as JPEG
        byte_io.seek(0)  # Move to the start of the byte stream

        # Predict the class of the image
        predicted_class = predict_image(byte_io)
        if not predicted_class:
            return jsonify({"error": "Prediction failed"}), 500

        # Extract category and fruit name
        category, fruit = predicted_class.split(' ', 1)

        # Parse the temperature input
        try:
            temperature = float(request.form['temperature']) + 273.15
        except (KeyError, ValueError):
            return jsonify({"error": "Invalid temperature value"}), 400

        # Prepare the database record
        life = 0 if category == "Bad" else predict_shelf_life(predicted_class, temperature)
        record = {
            "timestamp": datetime.now(),
            "temperature": round(temperature - 273.15, 2),
            "shelf_life": life,
            "category": category,
            "fruitname": fruit
        }

        # Insert the record into the database
        try:
            print("MongoDB instance:", mongo.db)
            mongo.db.predictions.insert_one(record)
        except Exception as db_error:
            print("Insertion error: ", str(db_error))
            return jsonify({
                "error": "Database insertion failed",
                "details": str(db_error)
            }), 500

        # Prepare and return response
        response = {
          "life": life,
          "name": fruit,
          "category": category,
          "temperature": temperature - 273.15
        }

        return jsonify(response)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500
