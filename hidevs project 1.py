
try:
    from deep_translator import GoogleTranslator
except ImportError:
    # Fallback translator if deep_translator is not available
    class GoogleTranslator:
        def __init__(self, source='auto', target='en'):
            self.source = source
            self.target = target
        def translate(self, text):
            # Fallback: return text unchanged
            return text

def translate_query(query):
    """Translate any language to English (fallback returns original text)."""
    try:
        translated_text = GoogleTranslator(source='auto', target='en').translate(query)
        return translated_text
    except Exception as e:
        return f"Translation error: {e}"

def generate_response(english_text):
    """Generate a simple predefined response."""
    return f"Your message in English: {english_text}\nThank you! A support agent will respond soon."

def multilingual_support():
    print("🌍 Multilingual Support Interface")
    print("Type 'exit' to stop.\n")

    while True:
        query = input("Enter your query in any language: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        english_text = translate_query(query)
        print("\nTranslated to English:")
        print(english_text)

        response = generate_response(english_text)
        print("\nSystem Response:")
        print(response)
        print("-" * 40)

if __name__ == "__main__":
    multilingual_support()

