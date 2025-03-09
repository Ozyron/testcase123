import unittest
from coe_6710110177.staircase import staircase

class TestStaircase(unittest.TestCase):

    def test_give_2_with_hash_should_be_hh(self):
        # Arrange
        n = 2
        pattern = '#'
        expected_output = "#\n##\n"
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_4_with_hash_should_be_hhhh(self):
        # Arrange
        n = 4
        pattern = '#'
        expected_output = "#\n##\n###\n####\n" 
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)
    
    def test_give_5_with_star_should_be_sssss(self):
        # Arrange
        n = 5
        pattern = '*'
        expected_output = "*\n**\n***\n****\n*****\n"
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)
    
    def test_give_3_with_plus_should_be_ppp(self):
        # Arrange
        n = 3
        pattern = '+'
        expected_output = "+\n++\n+++\n" 
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_4_with_double_char_pattern_should_be_abababab(self):
        # Arrange
        n = 4
        pattern = 'ab'
        expected_output = "ab\nabab\nababab\nabababab\n"
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_0_should_be_empty(self):
        # Arrange
        n = 0
        pattern = '#'
        expected_output = ""
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()