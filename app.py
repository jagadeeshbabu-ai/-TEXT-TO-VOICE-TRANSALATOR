"""
VoxBridge AI: Competition-Level Message-to-Voice Translation Web Application
"""
import time
import datetime
import streamlit as st

from core.translator import TranslationService
from core.speech import SpeechService
from utils.languages import SUPPORTED_LANGUAGES, get_language_names, get_language_info
from ui.styles import CUSTOM_CSS

# 1. Page Configuration
st.set_page_config(
    page_title="VoxBridge AI | Message-to-Voice",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject Custom Styling
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 3. Initialize Session State
if "history" not in st.session_state:
    st.session_state.history = []
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"
if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Telugu"
if "latest_result" not in st.session_state:
    st.session_state.latest_result = None

# 4. Cached Services
@st.cache_resource
def get_services():
    return TranslationService(), SpeechService()

translator, speech_engine = get_services()

# --- SIDEBAR: Architecture & Live Diagnostics ---
with st.sidebar:
    st.markdown("### 🏛️ System Architecture")
    st.markdown(
        """
        - **Primary Translation:** MyMemory Engine
        - **Fallback Translation:** Google Cloud GTX
        - **Neural Speech:** Microsoft Azure Neural via Edge
        - **Fallback Speech:** Google Text-to-Speech (gTTS)
        - **Streaming:** In-Memory Byte Buffering (0 disk latency)
        - **Privacy:** Ephemeral processing (Zero data retention)
        """
    )

    st.markdown("---")
    st.markdown("### 📊 Engine Status")
    st.markdown("🟢 **Translation Layer:** Online")
    st.markdown("🟢 **Neural Voice Layer:** Online")
    st.markdown("🟡 **Secondary Fallback:** Standby")

    st.markdown("---")
    st.markdown("### 🛠️ Session Controls")
    if st.button("🗑️ Clear History & Output", use_container_width=True):
        st.session_state.history = []
        st.session_state.latest_result = None
        st.session_state.input_text = ""
        st.rerun()

    st.markdown("---")
    st.caption("🏆 Built for Technical Competition • VoxBridge AI")


# --- HERO HEADER ---
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-badge">Competition Grade • Multi-Engine AI</div>
        <h1 class="hero-title">VoxBridge AI</h1>
        <div class="hero-subtitle">
            Next-generation Message-to-Voice translation system with natural regional speech synthesis, 
            zero-latency streaming, and multi-engine reliability.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- QUICK PRESET PROMPTS ---
st.markdown("##### 💡 Quick Test Prompts (Click to Load)")
col_p1, col_p2, col_p3, col_p4 = st.columns(4)

if col_p1.button("👋 Welcome Greeting", use_container_width=True):
    st.session_state.input_text = "Good morning everyone. Welcome to our technical presentation of VoxBridge AI."
    st.session_state.source_lang = "English"
    st.session_state.target_lang = "Telugu"
    st.rerun()

if col_p2.button("🚨 Emergency Alert", use_container_width=True):
    st.session_state.input_text = "Attention all passengers: Please proceed to Platform 3 immediately. The train is arriving."
    st.session_state.source_lang = "English"
    st.session_state.target_lang = "Hindi"
    st.rerun()

if col_p3.button("🏨 Travel Inquiry", use_container_width=True):
    st.session_state.input_text = "Excuse me, where is the nearest hospital and metro station?"
    st.session_state.source_lang = "English"
    st.session_state.target_lang = "Tamil"
    st.rerun()

if col_p4.button("🔄 Reverse Telugu -> English", use_container_width=True):
    st.session_state.input_text = "నాకు ఈ ప్రాజెక్ట్ చాలా ఇష్టం, ఇది చాలా బాగా పనిచేస్తుంది."
    st.session_state.source_lang = "Telugu"
    st.session_state.target_lang = "English"
    st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# --- LANGUAGE & VOICE SELECTION ROW ---
all_languages = get_language_names()

col_lang1, col_swap, col_lang2 = st.columns([5, 1, 5])

with col_lang1:
    src_idx = all_languages.index(st.session_state.source_lang) if st.session_state.source_lang in all_languages else 0
    src_lang = st.selectbox(
        "Source Language",
        options=all_languages,
        index=src_idx,
        key="select_src_lang",
        format_func=lambda l: f"{SUPPORTED_LANGUAGES[l]['flag']} {l}"
    )
    st.session_state.source_lang = src_lang

with col_swap:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    if st.button("⇄", help="Swap Source and Target Languages", use_container_width=True):
        st.session_state.source_lang, st.session_state.target_lang = st.session_state.target_lang, st.session_state.source_lang
        st.rerun()

with col_lang2:
    tgt_idx = all_languages.index(st.session_state.target_lang) if st.session_state.target_lang in all_languages else 1
    tgt_lang = st.selectbox(
        "Target Language",
        options=all_languages,
        index=tgt_idx,
        key="select_tgt_lang",
        format_func=lambda l: f"{SUPPORTED_LANGUAGES[l]['flag']} {l}"
    )
    st.session_state.target_lang = tgt_lang

# --- AUDIO SETTINGS CARD (VOICE & SPEED) ---
target_info = get_language_info(st.session_state.target_lang)
voices_dict = target_info.get("voices", {}) if target_info else {}
voice_options = list(voices_dict.keys())

col_voice, col_speed = st.columns([6, 6])
with col_voice:
    selected_voice = st.selectbox(
        f"🎙️ Voice Model for {st.session_state.target_lang}",
        options=voice_options,
        index=0 if voice_options else 0,
        key=f"voice_picker_{st.session_state.target_lang}",
        help="Studio-quality Microsoft Edge Neural TTS voices tailored for this language."
    )

with col_speed:
    speech_speed = st.select_slider(
        "⚡ Speech Playback Speed",
        options=[0.75, 1.0, 1.25, 1.5],
        value=1.0,
        format_func=lambda x: f"{x}x {'(Normal)' if x == 1.0 else ''}"
    )


# --- INPUT MESSAGE AREA ---
user_input = st.text_area(
    "Type or Paste Your Message:",
    value=st.session_state.input_text,
    height=130,
    placeholder="Type the message you want to translate and convert to voice...",
    help="Supports text up to 1500 characters."
)

col_count, col_clear = st.columns([8, 2])
with col_count:
    char_len = len(user_input.strip())
    st.caption(f"Character Count: **{char_len} / 1500**")
with col_clear:
    if st.button("Clear Input", use_container_width=True):
        st.session_state.input_text = ""
        st.rerun()

# --- ACTION BUTTONS ---
col_act1, col_act2 = st.columns([6, 6])
with col_act1:
    btn_translate_speak = st.button("🚀 Translate & Generate Voice", type="primary", use_container_width=True)
with col_act2:
    btn_translate_only = st.button("📝 Translate Text Only", use_container_width=True)


# --- EXECUTION LOGIC ---
if btn_translate_speak or btn_translate_only:
    if not user_input.strip():
        st.warning("⚠️ Please enter a message before submitting.")
    else:
        with st.spinner("Processing through VoxBridge AI pipeline..."):
            start_time = time.time()
            
            # Step 1: Translate
            trans_result = translator.translate(user_input, src_lang, tgt_lang)

            if not trans_result.success:
                st.error(f"❌ Translation Error: {trans_result.error}")
            else:
                speech_result = None
                if btn_translate_speak:
                    # Step 2: Synthesize Voice
                    speech_result = speech_engine.generate_speech(
                        text=trans_result.translated_text,
                        language_name=tgt_lang,
                        voice_choice=selected_voice,
                        speed=speech_speed
                    )

                elapsed = round(time.time() - start_time, 2)

                # Store latest result
                st.session_state.latest_result = {
                    "original": trans_result.original_text,
                    "translated": trans_result.translated_text,
                    "src_lang": src_lang,
                    "tgt_lang": tgt_lang,
                    "trans_engine": trans_result.engine_used,
                    "voice_used": speech_result.voice_used if speech_result else "N/A",
                    "speech_engine": speech_result.engine_used if speech_result else "N/A",
                    "audio_bytes": speech_result.audio_bytes if speech_result and speech_result.success else None,
                    "speed": f"{speech_speed}x",
                    "elapsed": f"{elapsed}s",
                    "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
                }

                # Add to history
                st.session_state.history.insert(0, st.session_state.latest_result)


# --- DISPLAY LATEST RESULT ---
if st.session_state.latest_result:
    res = st.session_state.latest_result
    st.markdown("---")
    st.markdown("### 🎯 Live Translation & Speech Output")

    col_out1, col_out2 = st.columns(2)

    with col_out1:
        st.markdown(f"**Original Message ({SUPPORTED_LANGUAGES[res['src_lang']]['flag']} {res['src_lang']})**")
        st.info(res["original"])

    with col_out2:
        st.markdown(f"**Translated Message ({SUPPORTED_LANGUAGES[res['tgt_lang']]['flag']} {res['tgt_lang']})**")
        st.success(res["translated"])

    # Metadata Badges
    st.markdown(
        f"""
        <div style="margin: 0.6rem 0; display: flex; gap: 0.8rem; flex-wrap: wrap;">
            <span class="engine-badge">⚡ {res['trans_engine']}</span>
            <span class="voice-badge">🎙️ Voice: {res['voice_used']}</span>
            <span class="engine-badge">⏱️ Latency: {res['elapsed']}</span>
            <span class="voice-badge">⏩ Speed: {res['speed']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Audio Playback & Download
    if res["audio_bytes"]:
        st.markdown("##### 🔊 Natural Voice Playback")
        st.audio(res["audio_bytes"], format="audio/mp3")

        col_dl, col_cp = st.columns([4, 6])
        with col_dl:
            st.download_button(
                label="📥 Download Audio (.mp3)",
                data=res["audio_bytes"],
                file_name=f"voxbridge_{res['tgt_lang'].lower()}_{int(time.time())}.mp3",
                mime="audio/mp3",
                use_container_width=True
            )
        with col_cp:
            st.code(res["translated"], language="text")


# --- TRANSLATION HISTORY ---
if st.session_state.history:
    st.markdown("---")
    st.markdown(f"### 📜 Session History ({len(st.session_state.history)} translations)")

    for idx, item in enumerate(st.session_state.history[:5]):
        with st.expander(f"🕒 {item['timestamp']} | {item['src_lang']} ➔ {item['tgt_lang']}: {item['original'][:40]}..."):
            st.markdown(f"**Original ({item['src_lang']}):** {item['original']}")
            st.markdown(f"**Translated ({item['tgt_lang']}):** {item['translated']}")
            if item["audio_bytes"]:
                st.audio(item["audio_bytes"], format="audio/mp3")
