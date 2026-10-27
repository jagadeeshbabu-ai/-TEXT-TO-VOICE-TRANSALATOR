# 🎙️ VoxBridge AI: Next-Gen Message-to-Voice Translation System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Competition Ready](https://img.shields.io/badge/Status-Competition%20Ready-success.svg)]()

> **VoxBridge AI** is an industry-grade Message-to-Voice Translation system designed for high reliability, multi-engine redundancy, and natural-sounding regional speech synthesis.

---

## 🌟 Key Differentiators (Why VoxBridge Beats Basic Projects)

| Feature | Typical Student Projects | **VoxBridge AI** |
| :--- | :--- | :--- |
| **Speech Quality** | Robotic, metallic concatenative TTS | **Microsoft Azure Neural TTS (`edge-tts`)** with human-like expressive cadence |
| **Regional Accents** | Monotone English-only fallback | **Native Regional Accents:** Telugu (`Shruti`, `Mohan`), Hindi (`Swara`, `Madhur`), Tamil (`Pallavi`), Indian English (`Neerja`, `Prabhat`) |
| **API Reliability** | Single fragile API (frequent 429 rate limits) | **Dual-Engine Redundancy:** MyMemory Primary with automatic Google Translate fallback |
| **Audio Pipeline** | Slow disk file writes (`.mp3` locks) | **In-Memory Streaming Buffers** (0 disk I/O bottleneck) |
| **Controls** | Basic static audio play | **Speed adjustments (0.75x to 1.5x)**, HTML5 scrub/seek, instant `.mp3` download |
| **Session Memory** | None (wipes on refresh) | **Session History Drawer** with replayable audio clips and timestamps |
| **Defensive Architecture** | Crashes on empty/whitespace inputs | **Strict input validation**, character counters, and identity translation short-circuiting |

---

## 🏛️ System Architecture

```text
[ User Text Input ]
        │
        ▼
[ Input Validator & Sanitizer ] ──(Invalid)──> [ User-Friendly Error Notice ]
        │ (Valid)
        ▼
[ Identity Translation Check ] ──(Same Lang)─> [ 0ms Instant Return ]
        │ (Different Lang)
        ▼
[ Primary Translation Engine ] ──(Fail/Limit)─> [ Fallback Engine (Google GTX) ]
   (MyMemory Translation)
        │ (Success)
        ▼
[ Neural Speech Synthesis Layer ] ──(Offline)──> [ Fallback Speech (gTTS) ]
 (Microsoft Edge Neural Voices)
        │
        ▼
[ In-Memory Audio Buffer (MP3) ]
        │
        ▼
[ Interactive UI: Play / Pause / Replay / Speed / Download / History ]
```

---

## 🌍 Supported Languages & Neural Voice Models

| Language | Flag | Primary Translation Code | Default Neural Voice | Available Speakers |
| :--- | :---: | :--- | :--- | :--- |
| **English** | 🇺🇸 / 🇮🇳 | `english` (`en`) | `en-US-AriaNeural` | Female (Aria), Male (Guy), Female (Neerja - IN), Male (Prabhat - IN) |
| **Telugu** | 🇮🇳 | `telugu` (`te`) | `te-IN-ShrutiNeural` | Female (Shruti), Male (Mohan) |
| **Hindi** | 🇮🇳 | `hindi` (`hi`) | `hi-IN-SwaraNeural` | Female (Swara), Male (Madhur) |
| **Tamil** | 🇮🇳 | `tamil india` (`ta`) | `ta-IN-PallaviNeural` | Female (Pallavi), Male (Valluvar) |
| **Kannada** | 🇮🇳 | `kannada` (`kn`) | `kn-IN-SapnaNeural` | Female (Sapna), Male (Gagan) |
| **Malayalam** | 🇮🇳 | `malayalam` (`ml`) | `ml-IN-SobhanaNeural` | Female (Sobhana), Male (Midhun) |
| **Spanish** | 🇪🇸 | `spanish` (`es`) | `es-ES-ElviraNeural` | Female (Elvira), Male (Alvaro) |
| **French** | 🇫🇷 | `french` (`fr`) | `fr-FR-DeniseNeural` | Female (Denise), Male (Henri) |
| **German** | 🇩🇪 | `german` (`de`) | `de-DE-KatjaNeural` | Female (Katja), Male (Killian) |
| **Japanese** | 🇯🇵 | `japanese` (`ja`) | `ja-JP-NanamiNeural` | Female (Nanami), Male (Keita) |

---

## 📂 Project Structure

```text
texttovoice/
├── app.py                 # Main Streamlit web application & UI
├── main.py                # Unified CLI & server launcher
├── pipeline.py            # End-to-end programmatic pipeline demo
├── requirements.txt       # Project dependencies
├── test_step1.py          # Translation service test suite
├── test_step2.py          # Neural TTS synthesis test suite
├── core/
│   ├── __init__.py
│   ├── translator.py      # Dual-engine translation service
│   └── speech.py          # High-fidelity Neural TTS service
├── utils/
│   ├── __init__.py
│   ├── languages.py       # Language registry & neural voice mapping
│   └── validator.py       # Input validation & sanitization
└── ui/
    ├── __init__.py
    └── styles.py          # Custom CSS theme & glassmorphic styling
```

---

## 🚀 Quick Start (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/jagadeeshbabu-ai/-TEXT-TO-VOICE-TRANSALATOR.git
cd -TEXT-TO-VOICE-TRANSALATOR
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python main.py
```
Or directly via Streamlit:
```bash
streamlit run app.py
```
Open your browser at **`http://localhost:8501`**.

---

## 🧪 Running Automated Tests

Run the full automated test suite covering translation accuracy, Telugu/Hindi/English neural speech, and defensive error boundaries:

```bash
python main.py --test
```

---

## ☁️ Deployment Guide (Streamlit Community Cloud)

1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **"New app"**.
3. Select your repository: `jagadeeshbabu-ai/-TEXT-TO-VOICE-TRANSALATOR`
4. Set **Branch**: `main`
5. Set **Main file path**: `app.py`
6. Click **Deploy!**
Your app will be live with a permanent public link (e.g. `https://voxbridge-ai.streamlit.app`).

---

## 🛡️ Privacy & Security

- **Zero Secret Exposure:** Requires no hardcoded API keys or external credentials.
- **Ephemeral Processing:** Text and generated audio are streamed in-memory and never persisted on external servers.

---

## 📜 License
This project is open-source under the [MIT License](LICENSE).
