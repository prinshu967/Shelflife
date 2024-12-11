from PIL import Image
import numpy as np
import tensorflow as tf
import os

# Load the pre-trained model
MODEL_PATH = r"app\model\New2Freshness50.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels (same as before)
class_labels = ['Bad Apple', 'Bad Banana', 'Bad Bellpepper', 'Bad Cucumber', 'Bad Grapes', 
                'Bad Indian Green Chile', 'Bad Mango', 'Bad Orange', 'Bad Potato', 'Bad Tomato', 
                'Fresh Apple', 'Fresh Banana', 'Fresh Bellpepper', 'Fresh Cucumber', 'Fresh Grapes', 
                'Fresh Indian Green Chile', 'Fresh Mango', 'Fresh Orange', 'Fresh Potato', 'Fresh Tomato', 
                'Moderate Apple', 'Moderate Banana', 'Moderate Bellpepper', 'Moderate Cucumber', 
                'Moderate Grapes', 'Moderate Indian Green Chile', 'Moderate Mango', 'Moderate Orange', 
                'Moderate Potato', 'Moderate Tomato']  # Add all labels

def load_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def predict_image(image_path):
    img_array = load_image(image_path)
    predictions = model.predict(img_array)
    return class_labels[np.argmax(predictions)]
