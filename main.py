#!/usr/bin/env python3
"""
TalentScout AI - Main Application Entry Point
Professional Hiring Assistant powered by AI
"""

import sys
import os
from pathlib import Path

# Add frontend to Python path
project_root = Path(__file__).parent
frontend_path = project_root / "frontend"
sys.path.insert(0, str(frontend_path))

def main():
    """Main entry point for TalentScout AI"""
    print("🎯 Starting TalentScout AI...")
    
    # Import and run the frontend app
    try:
        from frontend.app import main as frontend_main
        frontend_main()
    except ImportError as e:
        print(f"❌ Error importing frontend: {e}")
        print("Make sure you're running from the project root directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()