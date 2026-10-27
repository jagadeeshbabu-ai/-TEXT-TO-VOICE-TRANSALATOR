"""
Supported languages and mapping for Translation and Speech Engines.
Includes exact mapping for MyMemory, Google Translate Fallback, and Azure Neural TTS via edge-tts.
"""

SUPPORTED_LANGUAGES = {
    "English": {
        "trans_code": "english",
        "mymemory_code": "english",
        "google_code": "en",
        "tts_locale": "en-US",
        "flag": "🇺🇸",
        "default_voice": "en-US-AriaNeural",
        "voices": {
            "Female (Aria - US)": "en-US-AriaNeural",
            "Male (Guy - US)": "en-US-GuyNeural",
            "Female (Neerja - Indian)": "en-IN-NeerjaNeural",
            "Male (Prabhat - Indian)": "en-IN-PrabhatNeural",
        }
    },
    "Telugu": {
        "trans_code": "telugu",
        "mymemory_code": "telugu",
        "google_code": "te",
        "tts_locale": "te-IN",
        "flag": "🇮🇳",
        "default_voice": "te-IN-ShrutiNeural",
        "voices": {
            "Female (Shruti)": "te-IN-ShrutiNeural",
            "Male (Mohan)": "te-IN-MohanNeural",
        }
    },
    "Hindi": {
        "trans_code": "hindi",
        "mymemory_code": "hindi",
        "google_code": "hi",
        "tts_locale": "hi-IN",
        "flag": "🇮🇳",
        "default_voice": "hi-IN-SwaraNeural",
        "voices": {
            "Female (Swara)": "hi-IN-SwaraNeural",
            "Male (Madhur)": "hi-IN-MadhurNeural",
        }
    },
    "Tamil": {
        "trans_code": "tamil india",
        "mymemory_code": "tamil india",
        "google_code": "ta",
        "tts_locale": "ta-IN",
        "flag": "🇮🇳",
        "default_voice": "ta-IN-PallaviNeural",
        "voices": {
            "Female (Pallavi)": "ta-IN-PallaviNeural",
            "Male (Valluvar)": "ta-IN-ValluvarNeural",
        }
    },
    "Kannada": {
        "trans_code": "kannada",
        "mymemory_code": "kannada",
        "google_code": "kn",
        "tts_locale": "kn-IN",
        "flag": "🇮🇳",
        "default_voice": "kn-IN-SapnaNeural",
        "voices": {
            "Female (Sapna)": "kn-IN-SapnaNeural",
            "Male (Gagan)": "kn-IN-GaganNeural",
        }
    },
    "Malayalam": {
        "trans_code": "malayalam",
        "mymemory_code": "malayalam",
        "google_code": "ml",
        "tts_locale": "ml-IN",
        "flag": "🇮🇳",
        "default_voice": "ml-IN-SobhanaNeural",
        "voices": {
            "Female (Sobhana)": "ml-IN-SobhanaNeural",
            "Male (Midhun)": "ml-IN-MidhunNeural",
        }
    },
    "Spanish": {
        "trans_code": "spanish",
        "mymemory_code": "spanish",
        "google_code": "es",
        "tts_locale": "es-ES",
        "flag": "🇪🇸",
        "default_voice": "es-ES-ElviraNeural",
        "voices": {
            "Female (Elvira)": "es-ES-ElviraNeural",
            "Male (Alvaro)": "es-ES-AlvaroNeural",
        }
    },
    "French": {
        "trans_code": "french",
        "mymemory_code": "french",
        "google_code": "fr",
        "tts_locale": "fr-FR",
        "flag": "🇫🇷",
        "default_voice": "fr-FR-DeniseNeural",
        "voices": {
            "Female (Denise)": "fr-FR-DeniseNeural",
            "Male (Henri)": "fr-FR-HenriNeural",
        }
    },
    "German": {
        "trans_code": "german",
        "mymemory_code": "german",
        "google_code": "de",
        "tts_locale": "de-DE",
        "flag": "🇩🇪",
        "default_voice": "de-DE-KatjaNeural",
        "voices": {
            "Female (Katja)": "de-DE-KatjaNeural",
            "Male (Killian)": "de-DE-KillianNeural",
        }
    },
    "Japanese": {
        "trans_code": "japanese",
        "mymemory_code": "japanese",
        "google_code": "ja",
        "tts_locale": "ja-JP",
        "flag": "🇯🇵",
        "default_voice": "ja-JP-NanamiNeural",
        "voices": {
            "Female (Nanami)": "ja-JP-NanamiNeural",
            "Male (Keita)": "ja-JP-KeitaNeural",
        }
    }
}

def get_language_names():
    """Return list of human-readable language names."""
    return list(SUPPORTED_LANGUAGES.keys())

def get_language_info(lang_name: str):
    """Retrieve details for a specific language."""
    return SUPPORTED_LANGUAGES.get(lang_name, None)
