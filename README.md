Multilingual Support Interface
A lightweight, command-line multilingual translation and response system.

------------------------------------------------------------

Overview
This program allows users to enter text in any language. The system automatically attempts to translate the input into English and then generates a predefined support-style response.
A fallback translator ensures the program still works even if the deep_translator package is not installed.

------------------------------------------------------------

Features
- Automatic language detection and translation
- Safe fallback translator
- Predefined English support message
- Continuous CLI loop until user types "exit"

------------------------------------------------------------

Project File
hidevs project 1 (1).py

This file includes:
- Translation logic
- Fallback translator
- Command-line interface loop
- Response generator

------------------------------------------------------------

Installation (Optional)
pip install deep-translator

The script still works even without this package.

------------------------------------------------------------

Usage
Run the program with:
python "hidevs project 1 (1).py"

You will see:
"Multilingual Support Interface
Type 'exit' to stop."

------------------------------------------------------------

Example
User Input:
Hola, necesito ayuda con mi pedido.

Output:
Translated to English:
Hello, I need help with my order.

System Response:
Your message in English: Hello, I need help with my order.
Thank you! A support agent will respond soon.
