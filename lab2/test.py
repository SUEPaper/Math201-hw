import unittest
from operator import add, mul, mod
from lab2 import lambda_curry2, square_even_numbers, rule_numbers
from inspect import isfunction


class HomeWork1Test(unittest.TestCase):
    def test_lambda_curry2(self):
        self.assertEqual(isfunction(lambda_curry2(add)), True)
        self.assertEqual(isfunction(lambda_curry2(add)(3)), True)
        self.assertEqual(lambda_curry2(add)(3)(5), 8)

    def test_square_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(square_even_numbers(numbers), [4, 16, 36, 64])
        numbers1 = [2, 3, 32]
        self.assertEqual(square_even_numbers(numbers1), [4, 1024])

    def test_rule_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(rule_numbers(numbers), [2, 4, 4, 8, 6, 12, 8, 16, 10])
        numbers1 = [2, 3, 32]
        self.assertEqual(rule_numbers(numbers1), [4, 4, 64])


    
    

if __name__ == '__main__':
    unittest.main()