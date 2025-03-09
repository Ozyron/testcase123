import unittest
from coe_6710110177.alternating_characters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_characters(self):
        # Arrange
        s = 'AAAA'
        
        # Act
        result = alternating_characters(s)
        
        # Assert
        self.assertEqual(result, 3)

    def test_all_same_characters_b(self):
        # Arrange
        s = 'BBBBB'
        
        # Act
        result = alternating_characters(s)
        
        # Assert
        self.assertEqual(result, 4)

    def test_alternating_characters(self):
        # Arrange
        s = 'ABABABAB'
        
        # Act
        result = alternating_characters(s)
        
        # Assert
        self.assertEqual(result, 0)

    def test_alternating_characters_ba(self):
        # Arrange
        s = 'BABABA'
        
        # Act
        result = alternating_characters(s)
        
        # Assert
        self.assertEqual(result, 0)

    def test_mixed_characters(self):
        # Arrange
        s = 'AAABBB'
        
        # Act
        result = alternating_characters(s)
        
        # Assert
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
