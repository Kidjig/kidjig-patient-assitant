import speech_recognition as sr
from typing import Optional

class PatientVoice:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, audio_path: str) -> Optional[str]:
        """Transcribe audio file to text"""
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
                return self.recognizer.recognize_google(audio)
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return None