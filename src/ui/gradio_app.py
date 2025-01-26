import gradio as gr
from src.llm.voice_patient import record_audio_segment, transcribe_audio
from src.llm.doctor_brain import encode_image_to_base64, get_diagnosis
from src.llm.voice_doctor import tts_elevenlabs, tts_gTTS
from src.core.constants import SYSTEM_PROMPT


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
