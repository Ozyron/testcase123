import unittest
from coe_6710110177.caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesar_cipher('middle-Outz', 2), 'okffng-Qwvb')

    def test_case_2(self):
        self.assertEqual(caesar_cipher('Hello, World!', 5), 'Mjqqt, Btwqi!')

    def test_case_3(self):
        self.assertEqual(caesar_cipher('abc-XYZ', 3), 'def-ABC')

    def test_case_4(self):
        self.assertEqual(caesar_cipher('Python3.8', 10), 'Zidryx3.8')

    def test_case_5(self):
        self.assertEqual(caesar_cipher('No Change!', 0), 'No Change!')

if __name__ == '__main__':
    unittest.main()
