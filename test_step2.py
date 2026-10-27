"""
Step 2 Verification Test Suite: Neural Text-to-Speech Engine
"""
import sys
import os

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

from core.speech import SpeechService

def run_step2_tests():
    service = SpeechService()
    print("=" * 60)
    print("🔊 RUNNING STEP 2 NEURAL SPEECH TESTS")
    print("=" * 60)

    # Test 1: Telugu Neural Speech
    print("\n[Test 1] Telugu Neural Speech Synthesis:")
    telugu_text = "మా కాంపిటీషన్ ప్రాజెక్ట్ కు స్వాగతం."
    s1 = service.generate_speech(telugu_text, "Telugu")
    print(f"Status: {'✅ PASSED' if s1.success else '❌ FAILED'}")
    print(f"Engine: {s1.engine_used}")
    print(f"Voice: {s1.voice_used}")
    print(f"Audio Size: {len(s1.audio_bytes)} bytes")
    if s1.success:
        with open("sample_telugu.mp3", "wb") as f:
            f.write(s1.audio_bytes)
        print("Saved sample to: sample_telugu.mp3")

    # Test 2: Hindi Neural Speech
    print("\n[Test 2] Hindi Neural Speech Synthesis:")
    hindi_text = "आर्टिफिशियल इंटेलिजेंस हमारी दुनिया को बदल रहा है।"
    s2 = service.generate_speech(hindi_text, "Hindi")
    print(f"Status: {'✅ PASSED' if s2.success else '❌ FAILED'}")
    print(f"Engine: {s2.engine_used}")
    print(f"Voice: {s2.voice_used}")
    print(f"Audio Size: {len(s2.audio_bytes)} bytes")

    # Test 3: English Neural Speech with Speed Control (+25%)
    print("\n[Test 3] English Neural Speech with Speed Rate (1.25x):")
    en_text = "This is a demonstration of dynamic speech rate control."
    s3 = service.generate_speech(en_text, "English", speed=1.25)
    print(f"Status: {'✅ PASSED' if s3.success else '❌ FAILED'}")
    print(f"Engine: {s3.engine_used}")
    print(f"Voice: {s3.voice_used}")
    print(f"Rate: {s3.speed_rate}")
    print(f"Audio Size: {len(s3.audio_bytes)} bytes")

    # Test 4: Empty Text Validation
    print("\n[Test 4] Empty Input Audio Handling:")
    s4 = service.generate_speech("   ", "English")
    expected_fail = not s4.success and "whitespace" in (s4.error or "").lower()
    print(f"Status: {'✅ PASSED (Caught Gracefully)' if expected_fail else '❌ FAILED'}")
    print(f"Reported Error: {s4.error}")

    print("\n" + "=" * 60)
    all_passed = s1.success and s2.success and s3.success and expected_fail
    if all_passed:
        print("🎉 ALL STEP 2 TESTS PASSED SUCCESSFULLY!")
    else:
        print("⚠️ Some speech tests did not pass. Check details above.")
    print("=" * 60)

if __name__ == "__main__":
    run_step2_tests()
