import unittest
from coe_6710110177.caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_shift_middle_outz(self):
        # Arrange
        s = 'middle-Outz'
        k = 2
        
        # Act
        result = caesar_cipher(s, k)
        
        # Assert
        self.assertEqual(result, 'okffng-Qwvb')

    def test_shift_hello_world(self):
        # Arrange
        s = 'Hello, World!'
        k = 5
        
        # Act
        result = caesar_cipher(s, k)
        
        # Assert
        self.assertEqual(result, 'Mjqqt, Btwqi!')

    def test_shift_abc_xyz(self):
        # Arrange
        s = 'abc-XYZ'
        k = 3
        
        # Act
        result = caesar_cipher(s, k)
        
        # Assert
        self.assertEqual(result, 'def-ABC')

    def test_shift_python(self):
        # Arrange
        s = 'Python3.8'
        k = 10
        
        # Act
        result = caesar_cipher(s, k)
        
        # Assert
        self.assertEqual(result, 'Zidryx3.8')

    def test_no_shift(self):
        # Arrange
        s = 'No Change!'
        k = 0
        
        # Act
        result = caesar_cipher(s, k)
        
        # Assert
        self.assertEqual(result, 'No Change!')

if __name__ == '__main__':
    unittest.main()
