import unittest
from translator import french_to_english, english_to_french


class TranslatorTest(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french("Hey"), "Bonjour")

    def test_fr_to_en(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
