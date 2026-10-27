"""
Translation Service Layer: Handles multi-engine translation with automatic fallback.
"""
import html
import logging
from dataclasses import dataclass
from typing import Optional
from deep_translator import MyMemoryTranslator, GoogleTranslator
from utils.languages import get_language_info
from utils.validator import validate_input_text

logger = logging.getLogger(__name__)

@dataclass
class TranslationResult:
    success: bool
    original_text: str
    translated_text: str
    source_lang: str
    target_lang: str
    engine_used: str
    error: Optional[str] = None

class TranslationService:
    """
    Robust translation service that validates inputs and attempts multi-engine fallback.
    """

    def _clean_translated_text(self, text: str) -> str:
        """
        Cleans HTML artifacts and unescapes entities (e.g. &#39; -> ').
        """
        if not text:
            return ""
        unescaped = html.unescape(text)
        # Normalize double spaces
        return " ".join(unescaped.split())

    def translate(self, text: str, source_lang_name: str, target_lang_name: str) -> TranslationResult:
        """
        Translates input text from source language to target language.
        
        Args:
            text: The message to translate
            source_lang_name: Human readable language name (e.g., 'English', 'Telugu')
            target_lang_name: Human readable language name (e.g., 'Telugu', 'Hindi')
            
        Returns:
            TranslationResult with translation or error details
        """
        # Step 1: Input Validation
        is_valid, cleaned_text, val_err = validate_input_text(text)
        if not is_valid:
            return TranslationResult(
                success=False,
                original_text=text or "",
                translated_text="",
                source_lang=source_lang_name,
                target_lang=target_lang_name,
                engine_used="None",
                error=val_err
            )

        # Step 2: Language Info Lookup
        src_info = get_language_info(source_lang_name)
        tgt_info = get_language_info(target_lang_name)

        if not src_info:
            return TranslationResult(
                success=False,
                original_text=cleaned_text,
                translated_text="",
                source_lang=source_lang_name,
                target_lang=target_lang_name,
                engine_used="None",
                error=f"Source language '{source_lang_name}' is not supported."
            )

        if not tgt_info:
            return TranslationResult(
                success=False,
                original_text=cleaned_text,
                translated_text="",
                source_lang=source_lang_name,
                target_lang=target_lang_name,
                engine_used="None",
                error=f"Target language '{target_lang_name}' is not supported."
            )

        # Optimization: Same source and target
        if source_lang_name.lower() == target_lang_name.lower():
            return TranslationResult(
                success=True,
                original_text=cleaned_text,
                translated_text=cleaned_text,
                source_lang=source_lang_name,
                target_lang=target_lang_name,
                engine_used="Identity (No translation required)",
                error=None
            )

        # Step 3: Attempt Primary Engine (MyMemory)
        try:
            mm_src = src_info.get("mymemory_code", src_info.get("trans_code"))
            mm_tgt = tgt_info.get("mymemory_code", tgt_info.get("trans_code"))
            translator = MyMemoryTranslator(source=mm_src, target=mm_tgt)
            translated = translator.translate(cleaned_text)
            if translated and not translated.startswith("MYMEMORY WARNING:"):
                cleaned_result = self._clean_translated_text(translated)
                return TranslationResult(
                    success=True,
                    original_text=cleaned_text,
                    translated_text=cleaned_result,
                    source_lang=source_lang_name,
                    target_lang=target_lang_name,
                    engine_used="MyMemory Translation Engine",
                    error=None
                )
        except Exception as e:
            logger.warning("Primary engine (MyMemory) failed: %s. Trying fallback engine...", str(e))

        # Step 4: Attempt Fallback Engine (GoogleTranslator)
        try:
            g_src = src_info.get("google_code", "auto")
            g_tgt = tgt_info.get("google_code", "en")
            fallback = GoogleTranslator(source=g_src, target=g_tgt)
            translated = fallback.translate(cleaned_text)
            if translated:
                cleaned_result = self._clean_translated_text(translated)
                return TranslationResult(
                    success=True,
                    original_text=cleaned_text,
                    translated_text=cleaned_result,
                    source_lang=source_lang_name,
                    target_lang=target_lang_name,
                    engine_used="Google Translate (Fallback)",
                    error=None
                )
        except Exception as e:
            logger.error("Fallback engine (Google) also failed: %s", str(e))

        # Step 5: Graceful error response if all engines fail
        return TranslationResult(
            success=False,
            original_text=cleaned_text,
            translated_text="",
            source_lang=source_lang_name,
            target_lang=target_lang_name,
            engine_used="None",
            error="Translation service temporarily unavailable. Please check your internet connection or try again."
        )
