import unittest
from coe_6710110177.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizz(self):
        # Arrange
        x = 3
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, "Fizz")

    def test_fizz_multiple(self):
        # Arrange
        x1, x2, x3 = 6, 9, 12
        
        # Act
        result1 = fizzbuzz(x1)
        result2 = fizzbuzz(x2)
        result3 = fizzbuzz(x3)
        
        # Assert
        self.assertEqual(result1, "Fizz")
        self.assertEqual(result2, "Fizz")
        self.assertEqual(result3, "Fizz")
    
    def test_buzz(self):
        # Arrange
        x = 5
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, "Buzz")

    def test_buzz_multiple(self):
        # Arrange
        x1, x2, x3 = 10, 20, 25
        
        # Act
        result1 = fizzbuzz(x1)
        result2 = fizzbuzz(x2)
        result3 = fizzbuzz(x3)
        
        # Assert
        self.assertEqual(result1, "Buzz")
        self.assertEqual(result2, "Buzz")
        self.assertEqual(result3, "Buzz")

    def test_fizzbuzz(self):
        # Arrange
        x = 15
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, "FizzBuzz")

    def test_fizzbuzz_multiple(self):
        # Arrange
        x1, x2, x3 = 30, 45, 60
        
        # Act
        result1 = fizzbuzz(x1)
        result2 = fizzbuzz(x2)
        result3 = fizzbuzz(x3)
        
        # Assert
        self.assertEqual(result1, "FizzBuzz")
        self.assertEqual(result2, "FizzBuzz")
        self.assertEqual(result3, "FizzBuzz")
    
    def test_neither_fizz_nor_buzz(self):
        # Arrange
        x1, x2, x3, x4, x5 = 1, 2, 4, 7, 11
        
        # Act
        result1 = fizzbuzz(x1)
        result2 = fizzbuzz(x2)
        result3 = fizzbuzz(x3)
        result4 = fizzbuzz(x4)
        result5 = fizzbuzz(x5)
        
        # Assert
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 4)
        self.assertEqual(result4, 7)
        self.assertEqual(result5, 11)

    def test_zero(self):
        # Arrange
        x = 0
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, "FizzBuzz")

    def test_negative_number(self):
        # Arrange
        x1, x2, x3, x4 = -3, -5, -15, -1
        
        # Act
        result1 = fizzbuzz(x1)
        result2 = fizzbuzz(x2)
        result3 = fizzbuzz(x3)
        result4 = fizzbuzz(x4)
        
        # Assert
        self.assertEqual(result1, "Fizz")
        self.assertEqual(result2, "Buzz")
        self.assertEqual(result3, "FizzBuzz")
        self.assertEqual(result4, -1)

if __name__ == '__main__':
    unittest.main()
