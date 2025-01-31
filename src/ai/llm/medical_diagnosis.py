from groq import Groq
from typing import Optional
from src.core.prompts.medical_prompts import MedicalPrompts


class MedicalDiagnosis:
    def __init__(self):
        self.client = Groq()
        self.model = "llama-3.2-90b-vision-preview"

    def get_diagnosis(self, image_data: str, query: str) -> Optional[str]:
        """Get medical diagnosis from LLM based on image and query"""
        try:
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": MedicalPrompts.DIAGNOSIS + query},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_data}"
                            },
                        },
                    ],
                }
            ]

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error getting diagnosis: {e}")
            return None
