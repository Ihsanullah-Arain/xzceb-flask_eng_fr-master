"""Unit Test program for Translation"""
import unittest
from translator import french_to_english, english_to_french


class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        """Function for unit test for English to French Translation"""
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo')
        self.assertNotEqual(english_to_french("None"), '')

    def test_frenchToEnglish(self):
        """Function for unit test for French to English Translation"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english("None"), '')

if __name__ == '__main__':
    unittest.main()
