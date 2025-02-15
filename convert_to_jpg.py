# 📷 Image Processing Functions
# -------------------
import os
from PIL import Image



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

