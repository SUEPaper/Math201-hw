import unittest
from lab1 import falling


class HomeWork1Test(unittest.TestCase):
    def test_falling(self):
        self.assertEqual(falling(6,3), 120)
        self.assertEqual(falling(4,3), 24)
        self.assertEqual(falling(4,1), 4)
        self.assertEqual(falling(4,0), 1)

if __name__ == '__main__':
    unittest.main()