import unittest
from operator import add, mul, mod
from hw_python_data_structure import couple, largest_and_second
from inspect import isfunction


class HomeWork1Test(unittest.TestCase):
    def test_couple(self):
        self.assertEqual(couple([1, 2, 3], [4, 5, 6]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(couple(['c', 6], ['s', '1']), [['c', 's'], [6, '1']])
        self.assertEqual(couple(['c', 6], ['s', '1', 'A']), AssertionError)

    def test_largest_and_second(self):
        self.assertEqual(largest_and_second([1, 3, 5, 7, 10]), (10, 7))
        
if __name__ == '__main__':
    unittest.main()