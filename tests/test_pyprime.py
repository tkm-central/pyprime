# -*- coding: utf-8 -*-

import unittest

from pyprime import pyprime

class TestPyprime(unittest.TestCase):
    """
    Test for pyprime
    """

    def test_is_definitely_prime_1(self):
        actual = pyprime.is_definitely_prime(11)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_definitely_prime_2(self):
        actual = pyprime.is_definitely_prime(12)
        expected = False
        self.assertEqual(expected, actual)

    def test_is_definitely_prime_3(self):
        with self.assertRaises(ValueError):
            _ = pyprime.is_definitely_prime("string")

    def test_is_definitely_prime_4(self):
        with self.assertRaises(ValueError):
            _ = pyprime.is_definitely_prime(3.14)

    def test_is_definitely_prime_5(self):
        with self.assertRaises(ValueError):
            _ = pyprime.is_definitely_prime(-1)
    
    def test_is_probably_prime(self):
        with self.assertRaises(NotImplementedError):
            _ = pyprime.is_probably_prime(11)

    def test_is_certainly_prime(self):
        with self.assertRaises(NotImplementedError):
            _ = pyprime.is_certainly_prime(11)


if __name__ == '__main__':
    unittest.main()