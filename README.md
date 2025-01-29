# Medical AI Chatbot

An AI-powered medical assistant that combines voice interaction, image analysis, and natural language processing to provide preliminary medical assessments.

## Features
- 🎤 Voice interaction with patients
- 🩺 Medical image analysis
- 🔊 Text-to-speech response from doctor
- 🤖 Multi-modal AI processing (voice, image, text)

## Prerequisites

### System Requirements
#### macOS
```bash
# Install required system dependencies
brew install portaudio ffmpeg
```

#### Windows
- No additional system requirements needed.

#### Linux
```bash
# Install required system dependencies
sudo apt-get install portaudio19-dev python3-pyaudio ffmpeg
```

### Python Version
- Python 3.10 or higher (3.13 recommended)

### Package Manager Options

#### Option 1: Using `uv` (Recommended)
**Install uv:**
- **macOS:**
  Using Homebrew:
  ```bash
    brew install uv
  ```
  Use curl to download the script and execute it with sh
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Windows:**
  ```powershell
  irm https://astral.sh/uv/install.ps1 | iex
  ```

#### Option 2: Using `pip`
```bash
python -m pip install --upgrade pip
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kidjig/kidjig-patient-assitant-url
   cd medical-chatbot
   ```

2. **Create and activate a virtual environment:**
   - Using `uv`:
     ```bash
     uv venv
     source .venv/bin/activate  # macOS/Linux
     .\.venv\Scripts\activate  # Windows
     ```
   - Using `venv`:
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # macOS/Linux
     .\.venv\Scripts\activate  # Windows
     ```

3. **Install dependencies:**
   - Using `uv`:
     ```bash
     # Install dependencies from pyproject.toml
     uv install
     
     # Or install in editable mode
     uv pip install -e .
     ```
   
   - Using `pip`:
     ```bash
     # Install in editable mode
     pip install -e .
     ```

## Configuration

1. **Create environment file:**
   ```bash
   touch .env
   ```

2. **Add API keys to `.env`:**
   ```env
   GROQ_API_KEY=your_groq_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

## Project Structure
```
medical-chatbot/
├── src/
│   ├── ai/
│   │   ├── llm/          # LLM integration
│   │   ├── speech/       # Voice processing
│   │   └── vision/       # Image processing
│   ├── core/             # Core configurations
│   └── interface/        # User interface
├── data/
│   ├── external/         # External data
│   └── raw/              # Generated data
```

## Usage

1. **Run the application:**
   ```bash
   # Using uv
   uv run src/interface/gradio_app.py

   # Using Python
   python src/interface/gradio_app.py
   ```

2. **Open your browser:**
   - Local URL: `http://127.0.0.1:7860`
   - Interface capabilities:
     - Record voice input
     - Upload medical images
     - Receive AI-generated assessments
     - Listen to voice responses

## Dependencies
- `gradio`: Web interface
- `elevenlabs`: Text-to-speech
- `groq`: LLM provider
- `gtts`: Alternative TTS
- `speech_recognition`: Voice transcription
- `python-dotenv`: Environment management
- `pydantic`: Settings management

## Notes
⚠️ **Important Disclaimer**  
This is a demonstration project and **should not be used for actual medical diagnosis**.  
Always consult healthcare professionals for medical advice.  
API usage may incur costs (Groq/ElevenLabs).

---

### Platform-Specific Notes
**macOS**
- Uses `afplay` for audio playback
- Requires microphone permissions

**Windows**
- Uses default media player
- May need administrator privileges

**Linux**
- Requires `aplay` for audio playback
- May need additional audio packages


## Troubleshooting

### Dependency Issues
- If you encounter dependency conflicts:
  1. Create a new virtual environment
  2. Reinstall all dependencies
  3. Ensure package versions are compatible

### Permission Issues
- Verify the following permissions:
  - Microphone access
  - Internet connectivity
  - File system access for saving/loading

### API Key Errors
- Common API issues:
  - Check `.env` file exists
  - Verify API keys are correctly formatted
  - Ensure no extra spaces or quotes in keys
  - Validate API keys are active and valid
