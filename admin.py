from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
MODEL_PATH = 'model_2.h5'
model = load_model(MODEL_PATH)

# Define a function to preprocess the image &&&&&
def preprocess_image(image):
    target_size = (256, 256)  # Ensure this matches model.input_shape[1:3]
    image = image.resize(target_size)  # Resize image
    image = img_to_array(image)  # Convert to NumPy array
    image = image / 255.0  # Normalize pixel values
    
    # ✅ Keep 4D shape (batch_size, height, width, channels)
    image = np.expand_dims(image, axis=0)  # Model expects (1, 256, 256, 3)

    return image


class_labels = ['apple', 'banana', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'cucumber', 'garlic', 'ginger', 'grapes', 'lemon', 'onion', 'orange', 'potato', 'tomato']
@app.route('/predict', methods=['POST'])
def predict():
    try:  # ✅ Start Try Block
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files["image"]
        image = Image.open(io.BytesIO(file.read()))
        processed_image = preprocess_image(image)

        # Make prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction)  # Get index of highest probability
        confidence = float(np.max(prediction))  # Get confidence score

        # Convert predicted class index to actual label
        predicted_label = class_labels[predicted_class]

        return jsonify({
            "predicted_class": predicted_label,  # Return actual name, not index
            "confidence": confidence
        })

    except Exception as e:  # ✅ Correct placement
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
