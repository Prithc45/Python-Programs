import googletrans
'''pip install googletrans==4.0.0-rc1'''

from googletrans import Translator

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text

def main():
    text = input("Enter the text you want to translate: ")
    dest_lang = input("Enter the language code you want to translate into (e.g., fr for French): ")

    translated_text = translate_text(text, dest_lang)
    print("Translated text:", translated_text)

if __name__ == "__main__":
    main()