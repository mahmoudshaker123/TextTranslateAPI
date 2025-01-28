from translate import Translator

class TranslationService:
    _cache = {}
    
    @staticmethod
    def translate_text(text: str, target_language: str) -> dict:
        if (text, target_language) in TranslationService._cache:
            return TranslationService._cache[(text, target_language)]
        
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(text)
        
        # Debugging statements
        print(f"Translating '{text}' to '{target_language}'")
        print(f"Translated text: '{translated_text}'")

        TranslationService._cache[(text, target_language)] = {
            "original_text": text,
            "translated_text": translated_text,
            "target_language": target_language
        }
        return TranslationService._cache[(text, target_language)]