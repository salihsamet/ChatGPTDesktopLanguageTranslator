import openai
import os

def get_openai_api_key():
    # Ideally, you'd store your API key in an environment variable for security
    return os.getenv('OPENAI_API_KEY')

def translate_text(text, source_language, target_language):
    openai.api_key = get_openai_api_key()

    prompt = f"Translate the following text from {source_language} to {target_language}:\n\n{text}"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    translation_history = []

    print("Welcome to the Language Translator Console App!")
    print("Type 'exit' to quit the application.")
    print("Type 'history' to view the translation history.")
    print("Type 'change languages' to set a new source and target language.\n")

    source_language = input("Enter the source language (e.g., English): ")
    target_language = input("Enter the target language (e.g., Spanish): ")

    while True:
        text_to_translate = input("Enter the text to translate (or type 'exit' to quit, 'history' to view history, 'change languages' to change languages): ")

        if text_to_translate.lower() == 'exit':
            print("Goodbye!")
            break

        if text_to_translate.lower() == 'history':
            print("\nTranslation History:")
            for i, (src_lang, tgt_lang, original, translated) in enumerate(translation_history, 1):
                print(f"{i}. [{src_lang} -> {tgt_lang}] {original} -> {translated}")
            print()
            continue

        if text_to_translate.lower() == 'change languages':
            source_language = input("Enter the source language (e.g., English): ")
            target_language = input("Enter the target language (e.g., Spanish): ")
            continue

        translations = []
        for line in text_to_translate.split('\n'):
            translation = translate_text(line, source_language, target_language)
            translations.append((source_language, target_language, line, translation))

        for src_lang, tgt_lang, original, translated in translations:
            print(f"Translation: {translated}\n")
            translation_history.append((src_lang, tgt_lang, original, translated))

if __name__ == "__main__":
    main()
