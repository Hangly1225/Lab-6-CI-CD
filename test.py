import unittest
from main import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(12, 7), 19)
        self.assertEqual(self.calculator.add(11, 3), 14)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(30, 15), 15)
        self.assertEqual(self.calculator.subtract(22, 5), 17)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(12, 2), 24)
        self.assertEqual(self.calculator.multiply(32, 1), 32)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(22, 2), 11)
        self.assertEqual(self.calculator.divide(45, 5), 9)


if __name__ == "__main__":
    unittest.main()
