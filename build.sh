#!/bin/bash

set -e

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Error: virtual environment is not active. Run 'source venv/bin/activate' first."
    exit 1
fi

echo "Installing/upgrading PyInstaller..."
python -m pip install -U pyinstaller

echo "Building Instabot for Linux..."
pyinstaller Instabot_linux.spec

echo "Done! Binary available at: dist/Instabot/Instabot"
chmod +x dist/Instabot/Instabot
