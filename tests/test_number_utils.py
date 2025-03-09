from coe_6710110177.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):

    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        
    def test_empty_list(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime) 

    def test_single_prime(self):
        prime_list = [2]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_single_non_prime(self):
        prime_list = [4]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_mixed_prime_and_non_prime(self):
        prime_list = [2, 4, 7, 8, 13]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_large_prime_list(self):
        prime_list = [101, 103, 107, 109, 113]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_large_non_prime_list(self):
        prime_list = [100, 102, 104, 106, 108]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_large_mixed_prime_and_non_prime(self):
        prime_list = [101, 102, 103, 104, 105]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

if __name__ == '__main__':
    unittest.main()
