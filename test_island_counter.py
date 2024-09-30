import unittest
from island_counter import count_islands

class TestCountIslands(unittest.TestCase):
    def test_case_1(self):
        grid = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1]
        ]
        expected = 2
        self.assertEqual(count_islands(grid), expected)

    def test_case_2(self):
        grid = [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ]
        expected = 3
        self.assertEqual(count_islands(grid), expected)

    def test_case_3(self):
        grid = [
            [0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1]
        ]
        expected = 2
        self.assertEqual(count_islands(grid), expected)

    def test_single_zero(self):
        grid = [[0]]
        expected = 0
        self.assertEqual(count_islands(grid), expected)

    def test_single_one(self):
        grid = [[1]]
        expected = 1
        self.assertEqual(count_islands(grid), expected)

if __name__ == '__main__':
    unittest.main()
