
"""
    Translator
"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
        English to French
    """
    return MyMemoryTranslator(source="english", target="french").translate(english_text)


def french_to_english(french_text):
    """
        French to English
    """
    return MyMemoryTranslator(source="french", target="english").translate(french_text)
