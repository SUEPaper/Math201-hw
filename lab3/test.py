import unittest
from operator import add, mul, mod
from lab3 import count_cond, count_factors, cycle, fibonacci_list
from inspect import isfunction


class HomeWork1Test(unittest.TestCase):
    def test_count_factors(self):
        self.assertEqual(count_factors(6), 4)
        self.assertEqual(count_factors(4), 3)

    def test_count_cond(self):
        self.assertEqual(isfunction(count_cond(lambda n, i: n % i == 0)), True)
        self.assertEqual(count_cond(lambda n, i: n % i == 0)(2), 2)
        self.assertEqual(count_cond(lambda n, i: n % i == 0)(4), 3)
        self.assertEqual(count_cond(lambda n, i: n % i == 0)(12), 6)
        is_prime = lambda n, i: count_factors(i) == 2
        self.assertEqual(isfunction(count_cond(is_prime)), True)
        count_primes = count_cond(is_prime)
        self.assertEqual(count_primes(2), 1)
        self.assertEqual(count_primes(3), 2)
        self.assertEqual(count_primes(4), 2)
        self.assertEqual(count_primes(5), 3)
        self.assertEqual(count_primes(20), 8)

    def test_circle(self):
        def add1(x):
            return x + 1
        def times2(x):
            return x * 2
        def add3(x):
            return x + 3
        my_cycle = cycle(add1, times2, add3)
        self.assertEqual(isfunction(my_cycle), True)
        self.assertEqual(my_cycle(0)(5), 5)
        self.assertEqual(my_cycle(2)(1), 4)
        self.assertEqual(my_cycle(3)(2), 9)
        self.assertEqual(my_cycle(4)(2), 10)
        self.assertEqual(my_cycle(6)(1), 19)

    def test_fibonacci_list(self):
        def fibonacci_list_t(n):
            fib = lambda x: x if x <= 1 else fib(x-1) + fib(x-2)
            return [fib(i) for i in range(n)]
        self.assertEqual(fibonacci_list(10), fibonacci_list_t(10))
        self.assertEqual(fibonacci_list(8), fibonacci_list_t(8))
        self.assertEqual(fibonacci_list(4), fibonacci_list_t(4))


if __name__ == '__main__':
    unittest.main()