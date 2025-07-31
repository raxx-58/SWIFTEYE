SwiftEye - Image Classification Backend
Overview
This project implements the backend server for the SwiftEye image classification application. It utilizes a pre-trained TensorFlow/Keras model to analyze uploaded images and predict their categories (e.g., 'apple', 'banana', 'cabbage'). The server is built with Flask, providing a robust and scalable API for image prediction.

Features
Image Preprocessing: Automatically resizes and normalizes images to match the model's input requirements.

Deep Learning Prediction: Integrates a TensorFlow/Keras model (model_2.h5) for accurate image classification.

RESTful API: Provides a dedicated endpoint (/predict) for image classification requests.

CORS Enabled: Configured for Cross-Origin Resource Sharing, allowing seamless integration with various frontend applications.

Installation
Dependencies
Python 3.x

pip (Python package installer)

Required Python libraries: Flask, Flask-Cors, tensorflow, numpy, Pillow

Instructions
Clone the repository (if applicable):

git clone https://github.com/yourusername/swifteye-backend.git
cd swifteye-backend

Create a Virtual Environment (Recommended):

python -m venv venv

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install Flask Flask-Cors tensorflow numpy Pillow

Model File:
Ensure your trained model file, model_2.h5, is located in the same directory as admin.py. If your model file has a different name or path, please update the MODEL_PATH variable in admin.py accordingly.

Usage
Running the Flask Server
To start the backend server, navigate to the directory containing admin.py in your terminal and execute:

python admin.py

This command will launch the Flask server on http://0.0.0.0:5000. A web browser will automatically open to http://127.0.0.1:5000, which typically serves your Swifteye.html frontend (if present).

API Endpoint: /predict
The image classification API endpoint is accessible at http://127.0.0.1:5000/predict.

Method: POST

Content-Type: multipart/form-data

Body:

image: The image file (e.g., .jpg, .png) you wish to classify.

Example using curl:

curl -X POST -F "image=@/path/to/your/image.jpg" http://127.0.0.1:5000/predict

Successful Response (JSON):

{
    "predicted_class": "apple",
    "confidence": 0.987654321
}

Error Responses:

400 Bad Request:

{
    "error": "No image uploaded"
}

500 Internal Server Error:

{
    "error": "An error occurred during prediction: <error_details>"
}

Project Structure (Assumed)
admin.py: The core Flask application file.

model_2.h5: The pre-trained TensorFlow/Keras model used for predictions.

Swifteye.html (optional): The frontend HTML file, if your Flask app serves it directly.

Contributing
Contributions are welcome! Please feel free to fork this repository, implement improvements, and submit pull requests.

License
[Specify your license here, e.g., MIT License, Apache 2.0 License, etc.]
