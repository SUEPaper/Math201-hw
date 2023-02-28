import unittest
from lab1 import falling


class HomeWork1Test(unittest.TestCase):
    def test_falling1(self):
        self.assertEqual(falling(6,3), 120)
    
    def test_falling2(self):
        self.assertEqual(falling(4,3), 24)

    def test_falling3(self):
        self.assertEqual(falling(4,1), 4)

    def test_falling4(self):
        self.assertEqual(falling(4,0), 1)

if __name__ == '__main__':
    unittest.main()