# SwiftEye - Image Classification Backend

## Overview

This project implements the backend server for the SwiftEye image classification application. It leverages a pre-trained TensorFlow/Keras model to analyze uploaded images and accurately predict their categories (e.g., 'apple', 'banana', 'cabbage', 'tomato', etc.). Built with Flask, this server provides a robust and scalable API for image prediction, designed for seamless integration with a frontend application.

## Features

* **Image Preprocessing:** Automatically resizes and normalizes incoming images to meet the specific input requirements of the classification model.

* **Deep Learning Prediction:** Integrates a powerful TensorFlow/Keras model (`model_2.h5`) for high-accuracy image classification.

* **RESTful API:** Offers a dedicated and well-defined `/predict` endpoint for handling image classification requests.

* **CORS Enabled:** Configured for Cross-Origin Resource Sharing, ensuring smooth communication and integration with frontend applications hosted on different origins.

## Installation

### Dependencies

Before you begin, ensure you have the following installed:

* Python 3.x

* `pip` (Python package installer)

* Required Python libraries: `Flask`, `Flask-Cors`, `tensorflow`, `numpy`, `Pillow`

### Instructions

Follow these steps to set up and run the backend server:

1. **Clone the repository:**

   ```
   git clone [https://github.com/yourusername/swifteye-backend.git](https://github.com/yourusername/swifteye-backend.git)
   cd swifteye-backend
   
   ```

2. **Create a Virtual Environment (Recommended):**

   ```
   python -m venv venv
   
   ```

   * **On Windows:**

     ```
     .\venv\Scripts\activate
     
     ```

   * **On macOS/Linux:**

     ```
     source venv/bin/activate
     
     ```

3. **Install dependencies:**

   ```
   pip install Flask Flask-Cors tensorflow numpy Pillow
   
   ```

4. **Model File:**
   Ensure your trained model file, named `model_2.h5`, is placed in the same directory as `admin.py`. If your model file has a different name or path, please update the `MODEL_PATH` variable within `admin.py` accordingly.

## Usage

### Running the Flask Server

To start the backend server, navigate to the project's root directory (where `admin.py` is located) in your terminal and execute the following command:

```
python admin.py
