#!/usr/bin/env python3
"""
Setup script for Django Online Newspaper Project
This script automates the initial setup process
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Output: {e.output}")
        return False

def main():
    print("🚀 Setting up Django Online Newspaper Project")
    print("=" * 50)
    
    # Check if Python is available
    if not run_command("python3 --version", "Checking Python installation"):
        print("Please install Python 3.7+ to continue")
        sys.exit(1)
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("Failed to install dependencies. Please check your pip installation.")
        sys.exit(1)
    
    # Run migrations
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        print("Failed to create migrations")
        sys.exit(1)
    
    if not run_command("python manage.py migrate", "Applying migrations"):
        print("Failed to apply migrations")
        sys.exit(1)
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("Failed to collect static files")
        sys.exit(1)
    
    # Create superuser prompt
    print("\n🔐 Creating superuser account...")
    print("You'll be prompted to create an admin account for the Django admin panel.")
    try:
        subprocess.run("python manage.py createsuperuser", shell=True, check=True)
        print("✅ Superuser created successfully")
    except subprocess.CalledProcessError:
        print("⚠️  Superuser creation skipped or failed")
    
    print("\n🎉 Setup completed successfully!")
    print("\nTo start the development server, run:")
    print("python manage.py runserver")
    print("\nThen visit: http://127.0.0.1:8000")
    print("Admin panel: http://127.0.0.1:8000/admin")

if __name__ == "__main__":
    main()