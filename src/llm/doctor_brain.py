from dotenv import load_dotenv
from groq import Groq
import base64
# from core.config import Config

load_dotenv()

# GROQ_API_KEY = Config.GROQ_API_KEY

# Convert image to required format
image_path = "data/external/acne.jpeg"
image_file = open(image_path, "rb")
image_data = base64.b64encode(image_file.read()).decode("utf-8")

# Call Model
client = Groq()
llm = "llama-3.2-90b-vision-preview"

query = "What is the diagnosis of this image?"

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

response = client.chat.completions.create(
    model=llm,
    messages=messages,
)

content = response.choices[0].message.content
print(content)
