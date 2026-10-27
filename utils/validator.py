"""
Input validation and sanitization utilities.
"""
from typing import Tuple

MAX_TEXT_LENGTH = 1500

def validate_input_text(text: str) -> Tuple[bool, str, str]:
    """
    Validates and cleans input text before sending to translation services.
    
    Returns:
        (is_valid: bool, cleaned_text: str, error_message: str)
    """
    if not text:
        return False, "", "Input message cannot be empty. Please enter text to translate."
    
    cleaned = text.strip()
    
    if len(cleaned) == 0:
        return False, "", "Input message contains only whitespace. Please enter valid text."
        
    if len(cleaned) > MAX_TEXT_LENGTH:
        return False, "", f"Input exceeds maximum allowed length of {MAX_TEXT_LENGTH} characters (current: {len(cleaned)})."
        
    return True, cleaned, ""
