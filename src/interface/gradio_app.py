import gradio as gr
from src.ai.llm.medical_diagnosis import MedicalDiagnosis
from src.ai.speech.doctor_voice import DoctorVoice
from src.ai.speech.patient_voice import PatientVoice
from src.ai.vision.image_processor import ImageProcessor


class MedicalInterface:
    def __init__(self):
        self.diagnosis = MedicalDiagnosis()
        self.doctor = DoctorVoice()
        self.patient = PatientVoice()
        self.image_processor = ImageProcessor()

    def process_input(self, audio_filepath: str, image_filepath: str):
        """Process patient input and generate diagnosis"""
        try:
            # Step 1: Transcribe patient's voice
            if not audio_filepath:
                return "No audio recorded", "Please record your voice first", None

            transcribed_text = self.patient.transcribe_audio(audio_filepath)
            if not transcribed_text:
                return (
                    "Could not transcribe audio. Please try again.",
                    "Error processing input",
                    None,
                )

            # Step 2: Process image and get diagnosis
            if image_filepath and self.image_processor.validate_image(image_filepath):
                image_data = self.image_processor.encode_to_base64(image_filepath)
                doctor_response = self.diagnosis.get_diagnosis(
                    image_data, transcribed_text
                )
            else:
                doctor_response = "No image provided for analysis"

            # Step 3: Convert diagnosis to speech
            voice_response = self.doctor.text_to_speech_elevenlabs(
                doctor_response, "data/raw/doctor/doctor_response.mp3"
            )

            return transcribed_text, doctor_response, voice_response

        except Exception as e:
            print(f"Error in process_input: {e}")
            return "Error processing input", str(e), None

    def launch(self):
        """Launch the Gradio interface"""
        iface = gr.Interface(
            fn=self.process_input,
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
        iface.launch(debug=True, share=True)  # Added share=True for public access


if __name__ == "__main__":
    interface = MedicalInterface()
    interface.launch()
