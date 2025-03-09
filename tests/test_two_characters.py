import unittest
from coe_6710110177.two_characters import alternate

class TestTwoCharacters(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(alternate('beabeefeab'), 5)

    def test_alternating_characters(self):
        self.assertEqual(alternate('ababab'), 6)
        self.assertEqual(alternate('abcabcabc'), 6)
        self.assertEqual(alternate('ab'), 2)
    
    def test_repeating_characters(self):
        self.assertEqual(alternate('aabbcc'), 0)  
        self.assertEqual(alternate('aabb'), 0)   
        self.assertEqual(alternate('aabbccddeeff'), 0)  
        self.assertEqual(alternate('aabbccddeeffgghh'), 0)  
        self.assertEqual(alternate('aabbccddeeffgghhiijj'), 0)  
        self.assertEqual(alternate('aabbccddeeffgghhiijjkkll'), 0)  
        self.assertEqual(alternate('aabbccddeeffgghhiijjkkllmmnn'), 0) 
        self.assertEqual(alternate('aabbccddeeffgghhiijjkkllmmnnoopp'), 0)
        
    def test_single_character(self):
        self.assertEqual(alternate('a'), 0)
    
    def test_empty_string(self):
        self.assertEqual(alternate(''), 0)
    
    def test_mixed_characters(self):
        self.assertEqual(alternate('abcabc'), 4)
        self.assertEqual(alternate('abcdabcdabcd'), 6)

if __name__ == '__main__':
    unittest.main()