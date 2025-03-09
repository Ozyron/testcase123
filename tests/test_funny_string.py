import unittest
from coe_6710110177.funny_string import funny_string

class TestFunnyString(unittest.TestCase):

    def test_string_acxz_should_be_funny(self):
        # Arrange
        s = 'acxz'
        
        # Act
        result = funny_string(s)
        
        # Assert
        self.assertEqual(result, 'Funny')

    def test_string_bcxz_should_be_not_funny(self):
        # Arrange
        s = 'bcxz'
        
        # Act
        result = funny_string(s)
        
        # Assert
        self.assertEqual(result, 'Not Funny')

    def test_single_character_should_be_funny(self):
        # Arrange
        s = 'a'
        
        # Act
        result = funny_string(s)
        
        # Assert
        self.assertEqual(result, 'Funny')

    def test_two_identical_characters_should_be_funny(self):
        # Arrange
        s = 'aa'
        
        # Act
        result = funny_string(s)
        
        # Assert
        self.assertEqual(result, 'Funny')

    def test_two_different_characters_should_be_funny(self):
        # Arrange
        s = 'ab'
        
        # Act
        result = funny_string(s)
        
        # Assert
        self.assertEqual(result, 'Funny')

    def test_empty_string_should_be_funny(self):
        # Arrange
        s = ''
        
        # Act
        result = funny_string(s)
        
        # Assert
        self.assertEqual(result, 'Funny')

    def test_palindrome_string_should_be_funny(self):
        # Arrange
        s = 'madam'
        
        # Act
        result = funny_string(s)
        
        # Assert
        self.assertEqual(result, 'Funny')

if __name__ == '__main__':
    unittest.main()