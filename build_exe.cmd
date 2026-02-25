@echo off

if "%VIRTUAL_ENV%"=="" (
    echo Error: virtual environment is not active. Run 'venv\Scripts\activate' first.
    exit /b 1
)

echo Installing/upgrading PyInstaller...
python -m pip install -U pyinstaller

echo Building Instabot for Windows...
pyinstaller --onefile --onedir --icon="./assets/icon.ico" app.py --name Instabot

echo Done! Binary available at: dist\Instabot\Instabot.exe