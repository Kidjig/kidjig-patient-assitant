import os
from dotenv import load_dotenv
from src.core.config import Config
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform

load_dotenv()


# Function to convert text to speech using Google Text-to-Speech (gTTS) service
# Takes input text and output file path as parameters
# Generates an audio file in the specified language (English)
def tts_gTTS_old(input_text, output_file):
    language = "en"
    audio_obj = gTTS(text=input_text, lang=language, slow=False)

    audio_obj.save(output_file)


input_text = "Hello, how are you?"
gTTs_output_file = "data/raw/doctor/gtts_output.mp3"
# tts_gTTS_old(input_text, gTTs_output_file)


elevenlabs_output_file = "data/raw/doctor/ellabs_output.mp3"


# Function to convert text to speech using ElevenLabs Text-to-Speech service
# Takes input text and output file path as parameters
# Generates an audio file in the specified language (English)
def tts_elevenlabs_old(input_text, output_file):
    client = ElevenLabs(
        api_key=Config.ELEVENLABS_API_KEY,
    )
    audio = client.generate(
        text=input_text,
        voice="Aria",
        model="eleven_turbo_v2",
        output_format="mp3_22050_32",
    )
    elevenlabs.save(audio, elevenlabs_output_file)


# tts_elevenlabs_old(input_text, elevenlabs_output_file)


# With Autoplay
def tts_gTTS(input_text, output_file):
    language = "en"
    audio_obj = gTTS(text=input_text, lang=language, slow=False)

    audio_obj.save(output_file)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(["afplay", output_file])
        elif os_name == "Windows":  # Windows
            subprocess.run(
                [
                    "powershell",
                    "-c",
                    f'(New-Object Media.SoundPlayer "{output_file}").PlaySync();',
                ]
            )
        elif os_name == "Linux":  # Linux
            subprocess.run(
                ["aplay", output_file]
            )  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text = "Hello, how are you? Autoplay Testing"
gTTs_output_file = "data/raw/doctor/gtts_output_ap.mp3"
# tts_gTTS(input_text, gTTs_output_file)


elevenlabs_output_file = "data/raw/doctor/ellabs_output_ap.mp3"


# Function to convert text to speech using ElevenLabs Text-to-Speech service
# Takes input text and output file path as parameters
# Generates an audio file in the specified language (English)
def tts_elevenlabs(input_text, output_file):
    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )
    audio = client.generate(
        text=input_text,
        voice="Aria",
        model="eleven_turbo_v2",
        output_format="mp3_22050_32",
    )
    elevenlabs.save(audio, output_file)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # MacOS
            subprocess.run(["afplay", output_file])
        elif os_name == "Linux":  # Linux
            subprocess.run(["aplay", output_file])
        elif os_name == "Windows":  # Windows
            subprocess.run(["start", "", output_file])
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print("Error playing audio:", str(e))


# tts_elevenlabs(input_text, elevenlabs_output_file)
