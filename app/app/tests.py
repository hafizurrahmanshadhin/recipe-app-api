from django.test import TestCase
from app.calc import add


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together."""
        self.assertEqual(add(3, 8), 11)

    def test_add_negative_numbers(self):
        """Test that two negative numbers are added together."""
        self.assertEqual(add(-5, -7), -12)

    def test_add_positive_and_negative(self):
        """Test that a positive and a negative number are added together."""
        self.assertEqual(add(5, -3), 2)

    def test_add_zero(self):
        """Test that adding zero does not change the number."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)

    def test_add_floats(self):
        """Test that two float numbers are added together."""
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add(-1.1, 1.1), 0.0)

    def test_add_large_numbers(self):
        """Test that two large numbers are added together."""
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(add(-1000000, -2000000), -3000000)

    def test_add_mixed_types(self):
        """Test that adding an integer and a float works correctly."""
        self.assertAlmostEqual(add(5, 2.5), 7.5)
        self.assertAlmostEqual(add(3.5, 4), 7.5)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted correctly."""
        from app.calc import subtract
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
