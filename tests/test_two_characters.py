import unittest
from coe_6710110177.two_characters import alternate

class TestTwoCharacters(unittest.TestCase):
    def test_basic_case(self):
        # Arrange
        s = 'beabeefeab'
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, 5)

    def test_alternating_characters(self):
        # Arrange
        s1 = 'ababab'
        s2 = 'abcabcabc'
        s3 = 'ab'
        
        # Act
        result1 = alternate(s1)
        result2 = alternate(s2)
        result3 = alternate(s3)
        
        # Assert
        self.assertEqual(result1, 6)
        self.assertEqual(result2, 6)
        self.assertEqual(result3, 2)

    def test_repeating_characters(self):
        # Arrange
        s1 = 'aabbcc'
        s2 = 'aabb'
        s3 = 'aabbccddeeff'
        s4 = 'aabbccddeeffgghh'
        s5 = 'aabbccddeeffgghhiijj'
        s6 = 'aabbccddeeffgghhiijjkkll'
        s7 = 'aabbccddeeffgghhiijjkkllmmnn'
        s8 = 'aabbccddeeffgghhiijjkkllmmnnoopp'
        
        # Act
        result1 = alternate(s1)
        result2 = alternate(s2)
        result3 = alternate(s3)
        result4 = alternate(s4)
        result5 = alternate(s5)
        result6 = alternate(s6)
        result7 = alternate(s7)
        result8 = alternate(s8)
        
        # Assert
        self.assertEqual(result1, 0)
        self.assertEqual(result2, 0)
        self.assertEqual(result3, 0)
        self.assertEqual(result4, 0)
        self.assertEqual(result5, 0)
        self.assertEqual(result6, 0)
        self.assertEqual(result7, 0)
        self.assertEqual(result8, 0)
        
    def test_single_character(self):
        # Arrange
        s = 'a'
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, 0)
    
    def test_empty_string(self):
        # Arrange
        s = ''
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, 0)
    
    def test_mixed_characters(self):
        # Arrange
        s1 = 'abcabc'
        s2 = 'abcdabcdabcd'
        
        # Act
        result1 = alternate(s1)
        result2 = alternate(s2)
        
        # Assert
        self.assertEqual(result1, 4)
        self.assertEqual(result2, 6)

if __name__ == '__main__':
    unittest.main()