import unittest
from hw_pythoy_basics import falling, sum_digits, double_eights1, double_eights2


class HomeWork1Test(unittest.TestCase):
    def test_falling1(self):
        self.assertEqual(falling(6,3), 120)
    
    def test_falling2(self):
        self.assertEqual(falling(4,3), 24)

    def test_falling3(self):
        self.assertEqual(falling(4,1), 4)

    def test_falling4(self):
        self.assertEqual(falling(4,0), 1)

    def test_sum_digits1(self):
        self.assertEqual(sum_digits(10), 1)

    def test_sum_digits2(self):
        self.assertEqual(sum_digits(4224), 12)

    def test_sum_digits3(self):
        self.assertEqual(sum_digits(1234567890), 45)

    def test_sum_digits4(self):
        self.assertEqual(type(sum_digits(123)), int)

    def test_double_eights11(self):
        self.assertEqual(double_eights1(8), False)

    def test_double_eights12(self):
        self.assertEqual(double_eights1(88), True)

    def test_double_eights13(self):
        self.assertEqual(double_eights1(2882), True)

    def test_double_eights14(self):
        self.assertEqual(double_eights1(880088), True)

    def test_double_eights15(self):
        self.assertEqual(double_eights1(12345), False)
    
    def test_double_eights16(self):
        self.assertEqual(double_eights1(80808080), False)

    def test_double_eights21(self):
        self.assertEqual(double_eights2(8), False)

    def test_double_eights22(self):
        self.assertEqual(double_eights2(88), True)

    def test_double_eights23(self):
        self.assertEqual(double_eights2(2882), True)

    def test_double_eights24(self):
        self.assertEqual(double_eights2(880088), True)

    def test_double_eights25(self):
        self.assertEqual(double_eights2(12345), False)
    
    def test_double_eights26(self):
        self.assertEqual(double_eights2(80808080), False)

if __name__ == '__main__':
    unittest.main()