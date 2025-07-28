from elevenlabs import stream
from elevenlabs.client import ElevenLabs
from elevenlabs.core.api_error import ApiError
import os
from dotenv import load_dotenv
from logger import logger

load_dotenv()

try:
    elevenlabs = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))
except Exception as e:
    raise RuntimeError("Failed to initialize ElevenLabs client. Check your API key.") from e

def stream_audio(response_input: str):
    try:
        if not response_input.strip():
            logger.warning("⚠️ Empty response text. Skipping TTS.")
            return

        audio_stream = elevenlabs.text_to_speech.stream(
            text=response_input,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2"
        )
        stream(audio_stream)

    except ApiError as api_err:
        logger.error(f"ElevenLabs API error: {api_err}")

    except Exception as e:
        logger.error(f"Error in streaming audio: {e}")