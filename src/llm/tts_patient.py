import logging
from dotenv import load_dotenv
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Function to record an audio segment and save it as an MP3
def record_audio_segment(file_path, timeout=20, phrase_time_limit=None):
    """
    Record an audio segment from the microphone and save it to a file as an MP3.

    Args:
        file_path (str): Path to save the recorded audio file.
        timeout (int): Maximum time to wait for a phrase to start (in seconds).
        phrase_time_limit (int): Maximum time for a single phrase (in seconds).
    Returns:
        AudioSegment: Recorded audio segment.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Listening, Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start Speaking Now...")

            # Record audio segment
            audio = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
            )
            logging.info("Recording complete.")

            # Convert audio to AudioSegment
            audio_data = audio.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(audio_data))
            # Save audio segment as MP3
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")

    except sr.WaitTimeoutError:
        logging.warning("Timeout: No speech detected.")


audio_filepath = "data/raw/test.mp3"
# record_audio_segment(audio_filepath)

# Setup TTS to text-STT-model for transcription
# Call Model
client = Groq()
stt_llm = "whisper-large-v3"

audio_file = open(audio_filepath, "rb")
transcription = client.audio.transcriptions.create(
    model=stt_llm,
    file=audio_file,
    language="en",
)

print(transcription.text)
