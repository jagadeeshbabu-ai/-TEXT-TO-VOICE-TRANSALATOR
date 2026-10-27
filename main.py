"""
VoxBridge AI: Main Project Entrypoint
Usage:
    python main.py           -> Launches the Streamlit Web UI
    python main.py --cli     -> Runs interactive CLI demo
    python main.py --test    -> Runs automated test suites
"""
import sys
import os
import subprocess

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Check CLI flags
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ["--cli", "-c"]:
            cli_path = os.path.join(current_dir, "run_cli.py")
            subprocess.run([sys.executable, cli_path])
            return
        elif arg in ["--test", "-t"]:
            print("Running Step 1 & 2 Test Suites...")
            t1 = os.path.join(current_dir, "test_step1.py")
            t2 = os.path.join(current_dir, "test_step2.py")
            subprocess.run([sys.executable, t1])
            subprocess.run([sys.executable, t2])
            return
        elif arg in ["--help", "-h"]:
            print("VoxBridge AI - Help Menu")
            print("  python main.py          : Launch Web Application")
            print("  python main.py --cli    : Run Interactive Terminal CLI")
            print("  python main.py --test   : Run All Test Suites")
            return

    # Default action: Launch the Streamlit Web App
    app_path = os.path.join(current_dir, "app.py")
    print("=" * 60)
    print("🚀 LAUNCHING VOXBRIDGE AI WEB APPLICATION")
    print("=" * 60)
    print(f"Server Target: {app_path}")
    print("Access the app at: http://localhost:8501")
    print("=" * 60)

    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        app_path
    ])

if __name__ == "__main__":
    main()
