# 🎯 Object Detection Function
# -------------------
import os
from convert_to_jpg import convert_to_jpg
from dotenv import load_dotenv
load_dotenv(override=True)
api_key = os.getenv("API_key")  # Make sure variable names are inside quotes
api_url = "http://api.landing.ai/v1/tools/text-to-object-detection"

# Check if values are loaded correctly
print(f"API Key: {api_key}")
print(f"API URL: {api_url}")
import requests

def detect_objects(image_path):
    """
    Sends an image to the Landing AI API for object detection.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict or str: JSON response containing detected objects or an error message.
    """
    converted_image_path = convert_to_jpg(image_path)  # Ensure image is in JPG format
    
    with open(converted_image_path, "rb") as img:
        files = {"image": img}  # Use 'image' key instead of 'video'
        data = {
            "prompts": ["person", "garbage", "litter", "trash"],  # Object categories to detect
            "model": "owlv2",
            "function_name": "owl_v2_video"
        }
        headers = {"Authorization": f"Bearer {api_key}"}  # API Authentication

        response = requests.post(api_url, files=files, data=data, headers=headers)

        if response.status_code == 200:
            return response.json()  # Return detected objects
        else:
            return f"❌ Error {response.status_code}: {response.text}"