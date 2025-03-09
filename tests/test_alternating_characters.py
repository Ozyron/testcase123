import unittest
from coe_6710110177.alternating_characters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(alternating_characters('AAAA'), 3)

    def test_case_2(self):
        self.assertEqual(alternating_characters('BBBBB'), 4)

    def test_case_3(self):
        self.assertEqual(alternating_characters('ABABABAB'), 0)

    def test_case_4(self):
        self.assertEqual(alternating_characters('BABABA'), 0)

    def test_case_5(self):
        self.assertEqual(alternating_characters('AAABBB'), 4)

if __name__ == '__main__':
    
    
    
    
    unittest.main()
