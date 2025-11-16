# Multilingual → English Translator (Web GUI)

This project is a **simple web-based translation tool** built with **Python + Flask**.  
You can paste text in **any language**, and the app will translate it into **English**.

It opens in your **web browser**, so it works perfectly with **Python 3.13** (no Tkinter required).

## Features
- Paste any text (Hindi, Kannada, Telugu, Japanese, Arabic, French, etc.)
- Translates everything into **English**
- Automatically opens in your default browser
- Clean and simple web interface
- Works even without the translator library (fallback mode)
- Fully compatible with **Python 3.13** on Windows

## Project Files
```
multilingual_web.py       # Main translation app
```

## Requirements
Install these packages:
```
flask
deep-translator
```

## Installation

### 1. Create a virtual environment (recommended)
```
python -m venv .venv
```

Activate it (PowerShell):
```
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies
```
pip install flask deep-translator
```

## How to Run the Project
Run the script:
```
python multilingual_web.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

## How to Use
1. Paste or type any text in the Input box  
2. Click **Translate →**  
3. Read the English translation in the Output area  
4. Click **Clear** to reset both boxes  

## How It Works (Simple Explanation)
- The program runs a mini Flask server  
- You interact through your browser  
- It uses `deep_translator.GoogleTranslator` for translation  
- If translation fails, the input text is returned unchanged  

## Notes
- No Tkinter used → no Tcl/Tk errors on Python 3.13  
- No API keys required  
- Works offline  
- Safe fallback built-in  

## Future Improvements
- Select target language  
- Detect source language  
- Copy output button  
- Save translation history  
- Build EXE using `pyinstaller`
