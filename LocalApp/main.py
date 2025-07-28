from tutor import get_ai_response_with_history
from speechToText import start_transcription
from textToSpeech import stream_audio
from threading import Event
from logger import logger

is_speaking = Event()

def main():
    history: list[str] = []

    def handle_transcript(transcript: str):
        nonlocal history

        if is_speaking.is_set():
            return

        try:
            reply, history = get_ai_response_with_history(transcript, history, max_turns=2)
        except Exception as e:
            logger.error(f"AI error: {e}")
            return

        is_speaking.set()
        try:
            stream_audio(reply)
        except Exception as e:
            logger.warning(f"🔊 TTS error: {e}")
        finally:
            is_speaking.clear()

    start_transcription(
        on_transcript_callback=handle_transcript,
        mic_index=13,
        is_speaking=is_speaking.is_set
    )

if __name__ == "__main__":
    main()