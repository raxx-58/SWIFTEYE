import requests

url = "http://127.0.0.1:5000/predict"  # Flask API URL
image_path = "C:\Users\radhika mittal\SWIFTEYE\water.jpg"  # Path to your image

with open(image_path, "rb") as img:
    files = {"image": img}
    response = requests.post(url, files=files)

print(response.json())  # Print the API response
