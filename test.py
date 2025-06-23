import unittest
from main import remainder

class TestRemainder(unittest.TestCase):

    def test_remainder_success(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 5), 0)
        self.assertEqual(remainder(7, 4), 3)

    def test_remainder_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(5, 0)

if __name__ == '__main__':
    unittest.main()