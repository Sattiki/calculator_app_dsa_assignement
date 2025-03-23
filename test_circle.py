import unittest
import numpy as np
from circle import perform_calculation_circle, convert_to_float

class TestCircleCalculations(unittest.TestCase):

    def test_perimeter(self):
        """Test that the perimeter is calculated correctly."""
        radius = 5
        expected_perimeter = 2 * np.pi * radius
        result = perform_calculation_circle(radius, 'perimeter')
        self.assertAlmostEqual(result, expected_perimeter, places=5)

    def test_area(self):
        """Test that the area is calculated correctly."""
        radius = 5
        expected_area = np.pi * radius ** 2
        result = perform_calculation_circle(radius, 'area')
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_invalid_operation(self):
        """Test that an invalid operation raises a ValueError."""
        with self.assertRaises(ValueError):
            perform_calculation_circle(5, 'diameter')  # invalid input

    def test_convert_to_float_valid(self):
        """Test that convert_to_float correctly converts a string to float."""
        self.assertEqual(convert_to_float('3.14'), 3.14)

    def test_convert_to_float_invalid(self):
        """Test that convert_to_float raises a ValueError on invalid input."""
        with self.assertRaises(ValueError):
            convert_to_float('not_a_number')

if __name__ == '__main__':
    unittest.main()
