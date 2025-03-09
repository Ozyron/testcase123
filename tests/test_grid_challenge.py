import unittest
from coe_6710110177.grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    def test_sorted_rows_and_columns(self):
        # Arrange
        grid = [
            "ebacd",
            "fghij",
            "olmkn",
            "trpqs",
            "xywuv"
        ]
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, "YES")

    def test_sorted_rows_and_columns_small(self):
        # Arrange
        grid = [
            "abc",
            "ade",
            "efg"
        ]
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, "YES")

    def test_unsorted_columns(self):
        # Arrange
        grid = [
            "zyx",
            "wvu",
            "tsr"
        ]
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, "NO")

    def test_identical_rows(self):
        # Arrange
        grid = [
            "ppp",
            "ppp",
            "ppp"
        ]
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, "YES")

    def test_sorted_rows_and_columns_abc(self):
        # Arrange
        grid = [
            "abc",
            "bcd",
            "cde"
        ]
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, "YES")

    def test_unsorted_columns_abc(self):
        # Arrange
        grid = [
            "abd",
            "bce",
            "cad"
        ]
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, "NO")

if __name__ == '__main__':
    unittest.main()

