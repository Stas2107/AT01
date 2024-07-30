import unittest
from main import remainder

class TestMath(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(remainder(10, 3), 1)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError) as context:
            remainder(10, 0)
        self.assertEqual(str(context.exception), "Деление на ноль!")

    def test_zero_numerator(self):
        self.assertEqual(remainder(0, 10), 0)

    def test_identical_numbers(self):
        self.assertEqual(remainder(10, 10), 0)











    if __name__ == '__main__':
            unittest.main()