"""
Step 1 Verification Test Suite
"""
import sys

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

from core.translator import TranslationService

def run_tests():
    service = TranslationService()
    print("=" * 60)
    print("🚀 RUNNING STEP 1 TRANSLATION TESTS")
    print("=" * 60)

    # Test 1: English to Telugu
    print("\n[Test 1] English -> Telugu:")
    t1 = service.translate("Welcome to our competition project!", "English", "Telugu")
    print(f"Status: {'✅ PASSED' if t1.success else '❌ FAILED'}")
    print(f"Engine: {t1.engine_used}")
    print(f"Original: {t1.original_text}")
    print(f"Translated: {t1.translated_text}")

    # Test 2: Telugu to English
    print("\n[Test 2] Telugu -> English:")
    t2 = service.translate("శుభోదయం, మీరు ఎలా ఉన్నారు?", "Telugu", "English")
    print(f"Status: {'✅ PASSED' if t2.success else '❌ FAILED'}")
    print(f"Engine: {t2.engine_used}")
    print(f"Original: {t2.original_text}")
    print(f"Translated: {t2.translated_text}")

    # Test 3: English to Hindi
    print("\n[Test 3] English -> Hindi:")
    t3 = service.translate("Artificial intelligence is transforming our world.", "English", "Hindi")
    print(f"Status: {'✅ PASSED' if t3.success else '❌ FAILED'}")
    print(f"Engine: {t3.engine_used}")
    print(f"Original: {t3.original_text}")
    print(f"Translated: {t3.translated_text}")

    # Test 4: Empty string validation (Failure case handling)
    print("\n[Test 4] Empty Input Validation:")
    t4 = service.translate("   ", "English", "Telugu")
    expected_fail = not t4.success and "whitespace" in (t4.error or "").lower()
    print(f"Status: {'✅ PASSED (Caught Gracefully)' if expected_fail else '❌ FAILED'}")
    print(f"Reported Error: {t4.error}")

    # Test 5: Same Language (Optimization check)
    print("\n[Test 5] Same Source & Target Language:")
    t5 = service.translate("Hello world", "English", "English")
    is_identity = t5.success and t5.translated_text == "Hello world"
    print(f"Status: {'✅ PASSED' if is_identity else '❌ FAILED'}")
    print(f"Engine: {t5.engine_used}")

    print("\n" + "=" * 60)
    all_passed = t1.success and t2.success and t3.success and expected_fail and is_identity
    if all_passed:
        print("🎉 ALL STEP 1 TESTS PASSED SUCCESSFULLY!")
    else:
        print("⚠️ Some tests did not pass. Check output above.")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
