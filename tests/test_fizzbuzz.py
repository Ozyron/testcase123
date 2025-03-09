import unittest
from coe_6710110177.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_fizz_multiple(self):
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(12), "Fizz")
    
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_buzz_multiple(self):
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz(25), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_fizzbuzz_multiple(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")
        self.assertEqual(fizzbuzz(60), "FizzBuzz")
    
    def test_neither_fizz_nor_buzz(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz(7), 7)
        self.assertEqual(fizzbuzz(11), 11)

    def test_zero(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")

    def test_negative_number(self):
        self.assertEqual(fizzbuzz(-3), "Fizz")
        self.assertEqual(fizzbuzz(-5), "Buzz")
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
        self.assertEqual(fizzbuzz(-1), -1)

if __name__ == '__main__':
    unittest.main()
