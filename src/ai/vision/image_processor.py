import base64
from typing import Optional

class ImageProcessor:
    @staticmethod
    def encode_to_base64(image_path: str) -> Optional[str]:
        """Convert image to base64 encoding for LLM processing"""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

    @staticmethod
    def validate_image(image_path: str) -> bool:
        """Validate if the image file exists and is accessible"""
        try:
            with open(image_path, "rb") as _:
                return True
        except Exception:
            return False