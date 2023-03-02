import unittest
from lab1 import falling, sum_digits, double_eights1, double_eights2


class HomeWork1Test(unittest.TestCase):
    def test_falling(self):
        self.assertEqual(falling(6,3), 120)
        self.assertEqual(falling(4,3), 24)
        self.assertEqual(falling(4,1), 4)
        self.assertEqual(falling(4,0), 1)

    def test_sum_digits(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(4224), 12)
        self.assertEqual(sum_digits(1234567890), 45)
        self.assertEqual(type(sum_digits(123)), int)

    def test_double_eights1(self):
        self.assertEqual(double_eights1(8), False)
        self.assertEqual(double_eights1(88), True)
        self.assertEqual(double_eights1(2882), True)
        self.assertEqual(double_eights1(880088), True)
        self.assertEqual(double_eights1(12345), False)
        self.assertEqual(double_eights1(80808080), False)

    def test_double_eights2(self):
        self.assertEqual(double_eights2(8), False)
        self.assertEqual(double_eights2(88), True)
        self.assertEqual(double_eights2(2882), True)
        self.assertEqual(double_eights2(880088), True)
        self.assertEqual(double_eights2(12345), False)
        self.assertEqual(double_eights2(80808080), False)

if __name__ == '__main__':
    unittest.main()