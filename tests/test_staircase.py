import unittest
from coe_6710110177.staircase import staircase

class TestStaircase(unittest.TestCase):

    def test_give_2_with_hash_should_be_hh(self):
        #arrange
        n = 2
        pattern = '#'
        expected_output = "#\n##\n"

        #act
        result = staircase(n, pattern)

        #assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_4_with_hash_should_be_hhhh(self):
        #arrange
        n = 4
        pattern = '#'
        expected_output = "#\n##\n###\n####\n" 

        #act
        result = staircase(n, pattern)

        #assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_5_with_star_should_be_sssss(self):
        #arrange
        n = 5
        pattern = '*'
        expected_output = "*\n**\n***\n****\n*****\n"

        #act
        result = staircase(n, pattern)

        #assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_3_with_plus_should_be_ppp(self):
        #arrange
        n = 3
        pattern = '+'
        expected_output = "+\n++\n+++\n" 

        #act
        result = staircase(n, pattern)

        #assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_4_with_double_char_pattern_should_be_abababab(self):
        #arrange
        n = 4
        pattern = 'ab'
        expected_output = "ab\nabab\nababab\nabababab\n"

        #act
        result = staircase(n, pattern)

        #assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

if __name__ == '__main__':
    unittest.main()