import gradio as gr
from src.llm.voice_patient import record_audio_segment, transcribe_audio
from src.llm.doctor_brain import encode_image_to_base64, get_diagnosis
from src.llm.voice_doctor import tts_elevenlabs, tts_gTTS

print("Starting gradio app...")

# System prompt for medical chatbot
SYSTEM_PROMPT = """You are an experienced medical professional assistant. Your role is to:
1. Listen carefully to patient descriptions of symptoms and concerns
2. Analyze any medical images provided
3. Provide clear, professional medical assessments
4. Offer preliminary diagnoses and recommendations
5. Maintain patient confidentiality and medical ethics
6. Use appropriate medical terminology while remaining understandable
7. Acknowledge limitations and recommend professional medical consultation when necessary

Remember to:
- Stay within medical advisory scope
- Be empathetic yet professional
- Prioritize patient safety
- Be clear about the preliminary nature of any diagnosis
- Encourage proper medical follow-up
- Keep your answer concise (max 2 sentences)
- No preamble, start your answer right away please

Do not:
- Make definitive diagnoses
- Prescribe medications
- Replace professional medical consultation
- Provide emergency medical advice
"""

# SYSTEM_PROMPT = """You have to act as a professional doctor, i know you are not but this is for learning purpose.
#             What's in this image?. Do you find anything wrong with it medically?
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot,
#             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_input(audio_filepath, image_filepath):
    # Transcribe audio
    transcribed_text = transcribe_audio(audio_filepath)

    if image_filepath:
        doctor_response = get_diagnosis(
            image_data=encode_image_to_base64(image_filepath),
            query=SYSTEM_PROMPT + transcribed_text,
        )
    else:
        doctor_response = "No image provided for me to analyze"

    voice_doctor = tts_elevenlabs(
        input_text=doctor_response, output_file="data/raw/doctor/doctor_response.mp3"
    )

    return transcribed_text, doctor_response, voice_doctor


# Interface
iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Transcribed Text"),
        gr.Textbox(label="Diagnosis"),
        gr.Audio(label="Doctor's Response"),
    ],
    title="Voice Patient Assistant",
)
iface.launch(debug=True)
