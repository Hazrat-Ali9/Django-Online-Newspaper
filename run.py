#!/usr/bin/env python3
"""
Quick run script for Django Online Newspaper Project
"""

import subprocess
import sys
import os

def main():
    print("🚀 Starting Django Online Newspaper Server...")
    
    # Check if migrations are up to date
    try:
        result = subprocess.run(["python", "manage.py", "showmigrations", "--plan"], 
                              capture_output=True, text=True)
        if "[ ]" in result.stdout:
            print("📋 Applying pending migrations...")
            subprocess.run(["python", "manage.py", "migrate"], check=True)
    except:
        pass
    
    # Start the development server
    try:
        print("🌐 Server starting at http://127.0.0.1:8000")
        print("📊 Admin panel at http://127.0.0.1:8000/admin")
        print("Press Ctrl+C to stop the server")
        subprocess.run(["python", "manage.py", "runserver"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()