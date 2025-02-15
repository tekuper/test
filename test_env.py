# 📷 Image Processing Functions
# -------------------
import os
from PIL import Image
# 🎯 Object Detection Function
# -------------------
import os
from convert_to_jpg import convert_to_jpg
from dotenv import load_dotenv
load_dotenv(override=True)
api_key = os.getenv("API_key")  # Make sure variable names are inside quotes
api_url = "http://api.landing.ai/v1/tools/text-to-object-detection"

import requests





def convert_to_jpg(image_path):
    """
    
    Converts an image to JPG format if it's not already in that format.

    Args:
        image_path (str): Path to the input image.

    Returns:
        str: Path to the converted JPG image."""
    
    if image_path.lower().endswith(".jpg"):  # If already JPG, return as is
        return image_path

    img = Image.open(image_path)
    jpg_path = os.path.splitext(image_path)[0] + ".jpg"
    img.convert("RGB").save(jpg_path, "JPEG")
    
    return jpg_path






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