from flask import Flask, request, jsonify, send_from_directory
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import base64
import os

app = Flask(__name__, static_folder='static')

# Load the model from the repository root directory
MODEL_PATH = os.path.join(os.getcwd(), 'model.h5')
model = load_model(MODEL_PATH)

def prepare_image(image, target_size=(224, 224)):
    """Preprocess the image to match model requirements."""
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = np.array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/')
def index():
    # Serve the frontend HTML
    return send_from_directory(app.static_folder, 'Swifteye.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400
    
    # Expect image as a base64-encoded string (e.g., "data:image/png;base64,...")
    image_data = data['image']
    try:
        header, encoded = image_data.split(",", 1)
        decoded = base64.b64decode(encoded)
        image = Image.open(io.BytesIO(decoded))
    except Exception as e:
        return jsonify({'error': 'Invalid image data'}), 400

    processed_image = prepare_image(image)
    prediction = model.predict(processed_image)
    predicted_class = int(np.argmax(prediction, axis=1)[0])
    return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)

