import unittest

from algorithms.bit_manipulation.maximizing_xor import max_xor


class TestMaximizingXOR(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(max_xor(1, 10), 15)
        self.assertEqual(max_xor(10, 15), 7)


if __name__ == '__main__':
    unittest.main()
