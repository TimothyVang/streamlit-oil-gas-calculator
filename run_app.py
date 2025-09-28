#!/usr/bin/env python3
"""
BAH Jackson Sands Oil & Gas Investment Analysis
Alternative runner for local development

This file provides an alternative way to run the app locally.
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit app with proper configuration"""

    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Run Streamlit with the main app
    cmd = [
        sys.executable, "-m", "streamlit", "run",
        "app.py",
        "--server.port=8501",
        "--server.address=localhost",
        "--server.headless=false",
        "--browser.gatherUsageStats=false"
    ]

    print("🛢️ Starting BAH Jackson Sands Oil & Gas Investment Analysis...")
    print("📊 Opening application at http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")

    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()