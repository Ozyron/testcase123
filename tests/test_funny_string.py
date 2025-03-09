import unittest
from coe_6710110177.funny_string import funny_string

class TestFunnyString(unittest.TestCase):

    def test_string_acxz_should_be_funny(self):
        self.assertEqual(funny_string('acxz'), 'Funny')

    def test_string_bcxz_should_be_not_funny(self):
        self.assertEqual(funny_string('bcxz'), 'Not Funny')

    def test_single_character_should_be_funny(self):
        self.assertEqual(funny_string('a'), 'Funny')

    def test_two_identical_characters_should_be_funny(self):
        self.assertEqual(funny_string('aa'), 'Funny')

    def test_two_different_characters_should_be_funny(self):
        self.assertEqual(funny_string('ab'), 'Funny')

    def test_empty_string_should_be_funny(self):
        self.assertEqual(funny_string(''), 'Funny')

    def test_palindrome_string_should_be_funny(self):
        self.assertEqual(funny_string('madam'), 'Funny')

if __name__ == '__main__':
    unittest.main()