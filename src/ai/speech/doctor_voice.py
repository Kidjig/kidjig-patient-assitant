import os
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from gtts import gTTS
import subprocess
import platform

class DoctorVoice:
    def __init__(self):
        self.client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    def text_to_speech_elevenlabs(self, input_text: str, output_file: str) -> str:
        """Convert text to speech using ElevenLabs"""
        try:
            audio = self.client.generate(
                text=input_text,
                voice="Aria",
                model="eleven_turbo_v2",
                output_format="mp3_22050_32",
            )
            save(audio, output_file)  # Using elevenlabs.save instead of direct write
            self._play_audio(output_file)
            return output_file
        except Exception as e:
            print(f"Error in ElevenLabs TTS: {e}")
            return self.text_to_speech_gtts(input_text, output_file)

    def text_to_speech_gtts(self, input_text: str, output_file: str) -> str:
        """Fallback: Convert text to speech using Google TTS"""
        try:
            tts = gTTS(text=input_text, lang="en", slow=False)
            tts.save(output_file)
            self._play_audio(output_file)
            return output_file
        except Exception as e:
            print(f"Error in Google TTS: {e}")
            return ""

    def _play_audio(self, audio_file: str) -> None:
        """Play audio file based on operating system"""
        os_name = platform.system()
        try:
            if os_name == "Darwin":  # macOS
                subprocess.run(["afplay", audio_file])
            elif os_name == "Windows":
                subprocess.run(["start", "", audio_file], shell=True)
            elif os_name == "Linux":
                subprocess.run(["aplay", audio_file])
        except Exception as e:
            print(f"Error playing audio: {e}")

    def _save_and_play(self, audio, output_file: str) -> None:
        """Save and play audio file"""
        with open(output_file, 'wb') as f:
            f.write(audio)
        self._play_audio(output_file)