"""
Speech Synthesis Layer: Generates ultra-realistic neural audio with multi-engine fallback.
"""
import io
import asyncio
import logging
from dataclasses import dataclass
from typing import Optional
import edge_tts
from gtts import gTTS
from utils.languages import get_language_info
from utils.validator import validate_input_text

logger = logging.getLogger(__name__)

@dataclass
class SpeechResult:
    success: bool
    audio_bytes: bytes
    voice_used: str
    engine_used: str
    speed_rate: str
    error: Optional[str] = None

class SpeechService:
    """
    High-fidelity Neural Text-to-Speech service using Microsoft Edge Neural voices
    with automated fallback to Google Text-to-Speech (gTTS).
    """

    def __init__(self):
        pass

    def _format_rate(self, speed_multiplier: float) -> str:
        """
        Converts a numeric speed multiplier (e.g. 1.25) to edge-tts rate format (e.g. '+25%').
        """
        clamped = max(0.5, min(2.0, speed_multiplier))
        pct_change = int(round((clamped - 1.0) * 100))
        if pct_change >= 0:
            return f"+{pct_change}%"
        else:
            return f"{pct_change}%"

    async def _generate_edge_tts_async(self, text: str, voice: str, rate_str: str) -> bytes:
        """
        Streams neural audio bytes directly in memory.
        """
        communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate_str)
        audio_buffer = bytearray()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_buffer.extend(chunk["data"])
        return bytes(audio_buffer)

    def _generate_gtts_fallback(self, text: str, locale: str) -> bytes:
        """
        Generates standard TTS audio in memory using gTTS as a backup.
        """
        lang_code = locale.split("-")[0]
        fp = io.BytesIO()
        tts = gTTS(text=text, lang=lang_code)
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.read()

    def generate_speech(
        self,
        text: str,
        language_name: str,
        voice_choice: Optional[str] = None,
        speed: float = 1.0
    ) -> SpeechResult:
        """
        Synthesizes text into high quality audio.
        
        Args:
            text: Text to synthesize.
            language_name: Target language name (e.g. 'Telugu', 'Hindi', 'English').
            voice_choice: Optional voice key or voice identifier.
            speed: Playback speed multiplier (0.5 to 1.5, default 1.0).
            
        Returns:
            SpeechResult with raw audio bytes and metadata.
        """
        # Step 1: Input Validation
        is_valid, cleaned_text, val_err = validate_input_text(text)
        if not is_valid:
            return SpeechResult(
                success=False,
                audio_bytes=b"",
                voice_used="None",
                engine_used="None",
                speed_rate="+0%",
                error=val_err
            )

        lang_info = get_language_info(language_name)
        if not lang_info:
            return SpeechResult(
                success=False,
                audio_bytes=b"",
                voice_used="None",
                engine_used="None",
                speed_rate="+0%",
                error=f"Language '{language_name}' is not configured for speech synthesis."
            )

        # Step 2: Determine Voice & Rate
        available_voices = lang_info.get("voices", {})
        selected_voice = None
        if voice_choice and voice_choice in available_voices:
            selected_voice = available_voices[voice_choice]
        elif voice_choice and voice_choice in available_voices.values():
            selected_voice = voice_choice
        else:
            selected_voice = lang_info.get("default_voice", "en-US-AriaNeural")

        rate_str = self._format_rate(speed)

        # Step 3: Attempt Primary Neural Engine (edge-tts)
        try:
            # Handle event loop safely for both sync scripts and async frameworks
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(asyncio.run, self._generate_edge_tts_async(cleaned_text, selected_voice, rate_str))
                        audio_data = future.result()
                else:
                    audio_data = loop.run_until_complete(self._generate_edge_tts_async(cleaned_text, selected_voice, rate_str))
            except RuntimeError:
                audio_data = asyncio.run(self._generate_edge_tts_async(cleaned_text, selected_voice, rate_str))

            if audio_data and len(audio_data) > 0:
                return SpeechResult(
                    success=True,
                    audio_bytes=audio_data,
                    voice_used=selected_voice,
                    engine_used="Microsoft Edge Neural TTS",
                    speed_rate=rate_str,
                    error=None
                )
        except Exception as e:
            logger.warning("Primary neural TTS failed (%s). Attempting gTTS fallback...", str(e))

        # Step 4: Attempt Fallback Engine (gTTS)
        try:
            locale = lang_info.get("tts_locale", "en-US")
            audio_data = self._generate_gtts_fallback(cleaned_text, locale)
            if audio_data and len(audio_data) > 0:
                return SpeechResult(
                    success=True,
                    audio_bytes=audio_data,
                    voice_used="Standard Fallback Voice",
                    engine_used="Google Text-to-Speech (gTTS)",
                    speed_rate="Standard",
                    error=None
                )
        except Exception as e:
            logger.error("Fallback TTS engine also failed: %s", str(e))

        return SpeechResult(
            success=False,
            audio_bytes=b"",
            voice_used="None",
            engine_used="None",
            speed_rate=rate_str,
            error="Speech synthesis service unavailable. Please check your internet connection."
        )
