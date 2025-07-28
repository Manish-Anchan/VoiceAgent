from typing import Type, Callable, Iterator
import os
from dotenv import load_dotenv
import assemblyai as aai
from logger import logger

from assemblyai.streaming.v3 import (
    BeginEvent, StreamingClient, StreamingClientOptions,
    StreamingError, StreamingEvents, StreamingParameters,
    StreamingSessionParameters, TerminationEvent, TurnEvent
)

load_dotenv()
api_key = os.getenv("ASSEMBLYAI_API_KEY")

class PausableMicrophoneStream:
    def __init__(self, mic_stream: Iterator[bytes], is_speaking: Callable[[], bool]):
        self._mic = mic_stream
        self._is_speaking = is_speaking
        self._frame_size: int | None = None

    def __iter__(self):
        for chunk in self._mic:
            if self._frame_size is None:
                self._frame_size = len(chunk)

            if self._is_speaking():
                yield b"\x00" * self._frame_size
            else:
                yield chunk

def start_transcription(
    on_transcript_callback: Callable[[str], None],
    mic_index: int = 0,
    is_speaking: Callable[[], bool] = lambda: False
):
    def on_begin(self: Type[StreamingClient], event: BeginEvent):
        logger.info(f"🟢 Session started: {event.id}")

    def on_turn(self: Type[StreamingClient], event: TurnEvent):
        if event.end_of_turn and event.turn_is_formatted:
            transcript = event.transcript.strip()
            if not transcript:
                return
            if transcript.lower() in ["uh", "um", "hmm"]:
                return

            try:
                on_transcript_callback(transcript)
            except Exception as e:
                logger.error(f"⚠️ Error in transcript callback: {e}")

    def on_terminated(self: Type[StreamingClient], event: TerminationEvent):
        logger.info(f"Session terminated: {event.audio_duration_seconds}s processed")

    def on_error(self: Type[StreamingClient], error: StreamingError):
        logger.error(f"STT Error: {error}")

    client = StreamingClient(
        StreamingClientOptions(
            api_key=api_key,
            api_host="streaming.assemblyai.com",
        )
    )

    client.on(StreamingEvents.Begin, on_begin)
    client.on(StreamingEvents.Turn, on_turn)
    client.on(StreamingEvents.Termination, on_terminated)
    client.on(StreamingEvents.Error, on_error)

    client.connect(
        StreamingParameters(
            sample_rate=16000,
            format_turns=True,
        )
    )

    try:
        raw_mic = aai.extras.MicrophoneStream(sample_rate=16000, device_index=mic_index)
        wrapped_mic = PausableMicrophoneStream(raw_mic, is_speaking)
        logger.info("🎙️ Mic stream opened (pausable).")
        client.stream(wrapped_mic)
    except Exception as e:
        logger.error(f"🎤 Microphone error: {e}")
    finally:
        client.disconnect(terminate=True)
        logger.info("🔌 STT disconnected.")