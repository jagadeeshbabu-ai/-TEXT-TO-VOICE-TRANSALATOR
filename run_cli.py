"""
Interactive CLI for VoxBridge AI Translation
"""
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

from core.translator import TranslationService
from utils.languages import get_language_names

def interactive_cli():
    service = TranslationService()
    languages = get_language_names()

    print("=" * 65)
    print(" 🌐  VOXBRIDGE AI - MESSAGE TRANSLATION ENGINE (CLI DEMO)")
    print("=" * 65)
    print("Available languages:", ", ".join(languages))
    print("-" * 65)

    # Demo default translation
    sample_text = "Welcome to our technical presentation. We are happy to demonstrate our project."
    src = "English"
    tgt = "Telugu"

    print(f"\n[DEMO TRANSLATION]")
    print(f"Source Language : {src}")
    print(f"Target Language : {tgt}")
    print(f"Input Message   : '{sample_text}'")
    print("\nTranslating...")

    res = service.translate(sample_text, src, tgt)
    if res.success:
        print(f"\n[RESULT]")
        print(f"Translated Text : {res.translated_text}")
        print(f"Engine Used     : {res.engine_used}")
    else:
        print(f"\n[ERROR]: {res.error}")

    print("\n" + "=" * 65)

if __name__ == "__main__":
    interactive_cli()
