# from dotenv import load_dotenv
from groq import Groq
import base64
from src.core.config import Config

# load_dotenv()

GROQ_API_KEY = Config.GROQ_API_KEY


llm = "llama-3.2-90b-vision-preview"


# Convert image to required format
def encode_image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Call Model
def get_diagnosis(
    image_data: str,
    query: str,
) -> str:
    """
    Get diagnosis from an image using Groq LLM

    Args:
        image_data: Base64 encoded image data
        query: Question to ask about the image

    Returns:
        str: Model's diagnosis response
    """
    client = Groq()
    llm = "llama-3.2-90b-vision-preview"
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                },
            ],
        }
    ]

    try:
        response = client.chat.completions.create(
            model=llm,
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error getting diagnosis: {str(e)}"
