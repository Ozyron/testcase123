import unittest
from coe_6710110177.cat_and_mouse import cat_and_mouse

class TestCatAndMouse(unittest.TestCase):

    def test_cat_a_reaches_first(self):
        # arrange
        x = 1
        y = 5
        z = 2
        expected_output = "Cat A"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Cat A should reach first")

    def test_cat_b_reaches_first(self):
        # arrange
        x = 1
        y = 5
        z = 4
        expected_output = "Cat B"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Cat B should reach first")

    def test_both_cats_reach_simultaneously(self):
        # arrange
        x = 1
        y = 5
        z = 3
        expected_output = "Mouse C"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Mouse should escape")

    def test_cats_start_at_same_position(self):
        # arrange
        x = 2
        y = 2
        z = 1
        expected_output = "Mouse C"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Mouse should escape")

    def test_mouse_at_cat_b_position(self):
        # arrange
        x = 1
        y = 5
        z = 5
        expected_output = "Cat B"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Cat B should catch the mouse")

    def test_mouse_at_cat_a_position(self):
        # arrange
        x = 1
        y = 5
        z = 1
        expected_output = "Cat A"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Cat A should catch the mouse")

    def test_all_at_same_position(self):
        # arrange
        x = 1
        y = 1
        z = 1
        expected_output = "Mouse C"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Mouse should escape")

    def test_mouse_between_cats(self):
        # arrange
        x = 1
        y = 5
        z = 3
        expected_output = "Mouse C"
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Mouse should escape")

    def test_mouse_far_from_cats(self):
    # arrange
        x = 1
        y = 5
        z = 10
        expected_output = "Cat B"  # FIXED EXPECTED OUTPUT
        
        # act
        result = cat_and_mouse(x, y, z)
        
        # assert
        self.assertEqual(result, expected_output, "Cat B should catch the mouse")

if __name__ == '__main__':
    unittest.main()








