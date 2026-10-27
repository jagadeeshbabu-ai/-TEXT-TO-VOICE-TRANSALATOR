"""
End-to-End Pipeline: Message Input -> Multi-Engine Translation -> Neural Speech Synthesis
"""
import sys
import os

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

from core.translator import TranslationService
from core.speech import SpeechService

def run_pipeline(
    message: str,
    source_language: str,
    target_language: str,
    voice_choice: str = None,
    speed: float = 1.0,
    output_audio_file: str = "output.mp3"
):
    print("=" * 65)
    print(" 🚀 VOXBRIDGE AI: END-TO-END PIPELINE DEMO")
    print("=" * 65)
    print(f"Input Message    : '{message}'")
    print(f"Source Language  : {source_language}")
    print(f"Target Language  : {target_language}")
    print(f"Speed Multiplier : {speed}x")
    print("-" * 65)

    # 1. Translate
    print("\n[Step 1] Translating message...")
    translator = TranslationService()
    trans_res = translator.translate(message, source_language, target_language)

    if not trans_res.success:
        print(f"❌ Translation Failed: {trans_res.error}")
        return False

    print(f"✅ Translation Success!")
    print(f"Translated Text  : {trans_res.translated_text}")
    print(f"Engine Used      : {trans_res.engine_used}")

    # 2. Synthesize Speech
    print("\n[Step 2] Synthesizing Neural Audio...")
    speech_service = SpeechService()
    speech_res = speech_service.generate_speech(
        text=trans_res.translated_text,
        language_name=target_language,
        voice_choice=voice_choice,
        speed=speed
    )

    if not speech_res.success:
        print(f"❌ Speech Synthesis Failed: {speech_res.error}")
        return False

    with open(output_audio_file, "wb") as f:
        f.write(speech_res.audio_bytes)

    print(f"✅ Speech Generation Success!")
    print(f"Voice Utilized   : {speech_res.voice_used}")
    print(f"Engine Used      : {speech_res.engine_used}")
    print(f"Output File      : {output_audio_file} ({len(speech_res.audio_bytes)} bytes)")
    print("=" * 65)
    return True

if __name__ == "__main__":
    # Test sample: English to Telugu with Neural Voice
    sample_text = "Good morning everyone. Welcome to our live demonstration of VoxBridge AI."
    run_pipeline(sample_text, "English", "Telugu", output_audio_file="demo_telugu.mp3")
