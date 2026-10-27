"""
Custom styling and aesthetic theme for VoxBridge AI.
"""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Gradient Header Hero */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
        padding: 2.2rem 2.5rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px -10px rgba(79, 70, 229, 0.3);
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.25);
        border: 1px solid rgba(165, 180, 252, 0.4);
        color: #c7d2fe;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(to right, #ffffff, #c7d2fe, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        margin-top: 0.5rem;
        max-width: 650px;
        line-height: 1.5;
    }

    /* Result Card */
    .result-box {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 1.4rem;
        margin-top: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    .engine-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 8px;
        padding: 0.25rem 0.6rem;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .voice-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: rgba(99, 102, 241, 0.15);
        color: #a5b4fc;
        border: 1px solid rgba(165, 180, 252, 0.3);
        border-radius: 8px;
        padding: 0.25rem 0.6rem;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Quick Preset Buttons */
    .preset-chip {
        display: inline-block;
        background: #1e293b;
        color: #e2e8f0;
        padding: 0.4rem 0.8rem;
        border-radius: 10px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        cursor: pointer;
    }

    /* Translation Text Highlighting */
    .translated-text {
        font-size: 1.35rem;
        font-weight: 600;
        color: #f8fafc;
        line-height: 1.6;
        margin: 0.8rem 0;
        padding: 1rem;
        background: rgba(30, 41, 59, 0.7);
        border-radius: 10px;
        border-left: 4px solid #6366f1;
    }

    /* History Cards */
    .history-card {
        background: #1e293b;
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        margin-bottom: 0.75rem;
        border: 1px solid #334155;
    }

    .history-meta {
        font-size: 0.75rem;
        color: #94a3b8;
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.3rem;
    }
</style>
"""
