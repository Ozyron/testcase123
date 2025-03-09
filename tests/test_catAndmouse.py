import unittest
from coe_6710110177.cat_and_mouse import cat_and_mouse

class TestCatAndMouse(unittest.TestCase):

    def test_cat_a_reaches_first(self):
        # Arrange
        x, y, z = 1, 5, 2
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_b_reaches_first(self):
        # Arrange
        x, y, z = 1, 5, 4
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Cat B")

    def test_both_cats_reach_simultaneously(self):
        # Arrange
        x, y, z = 1, 5, 3
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Mouse C")

    def test_cats_start_at_same_position(self):
        # Arrange
        x, y, z = 2, 2, 1
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_at_cat_b_position(self):
        # Arrange
        x, y, z = 1, 5, 5
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Cat B")

    def test_mouse_at_cat_a_position(self):
        # Arrange
        x, y, z = 1, 5, 1
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Cat A")

    def test_all_at_same_position(self):
        # Arrange
        x, y, z = 1, 1, 1
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_between_cats(self):
        # Arrange
        x, y, z = 1, 5, 3
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_far_from_cats(self):
        # Arrange
        x, y, z = 1, 5, 10
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, "Cat B")

if __name__ == '__main__':
    unittest.main()








