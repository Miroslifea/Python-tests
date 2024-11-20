import unittest
import math
from GeometricFunctions import *

class TestGeometryFunctions(unittest.TestCase):

    '''Позитивные тесты'''

    def test_circle_area_positive(self):
        self.assertAlmostEqual(circleArea(1), math.pi)
        self.assertAlmostEqual(circleArea(2), 4 * math.pi)

    def test_circle_perimeter_positive(self):
        self.assertAlmostEqual(circlePerimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circlePerimeter(2), 4 * math.pi)

    def test_rectangle_area_positive(self):
        self.assertEqual(rectangleArea(2, 3), 6)
        self.assertEqual(rectangleArea(5, 5), 25)

    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectanglePerimeter(2, 3), 10)
        self.assertEqual(rectanglePerimeter(5, 5), 20)

    def test_square_area_positive(self):
        self.assertEqual(squareArea(3), 9)
        self.assertEqual(squareArea(5), 25)

    def test_square_perimeter_positive(self):
        self.assertEqual(squarePerimeter(3), 12)
        self.assertEqual(squarePerimeter(5), 20)

    def test_triangle_area_positive(self):
        self.assertEqual(traingleArea(4, 3), 6)
        self.assertEqual(traingleArea(10, 5), 25)

    def test_triangle_perimeter_positive(self):
        self.assertEqual(trainglePerimeter(3, 4, 5), 12)
        self.assertEqual(trainglePerimeter(7, 8, 9), 24)

    '''Негативные тесты'''

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            circleArea(-1)

    def test_rectangle_area_negative(self):
        with self.assertRaises(ValueError):
            rectangleArea(-2, 3)

    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            squareArea(-3)

    def test_triangle_area_negative(self):
        with self.assertRaises(ValueError):
            traingleArea(4, -3)

    def test_triangle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            trainglePerimeter(3, -4, 5)

    '''Граничные тесты'''

    def test_circle_area_boundary(self):
        self.assertEqual(circleArea(0), 0)

    def test_rectangle_area_boundary(self):
        self.assertEqual(rectangleArea(0, 5), 0)
        self.assertEqual(rectangleArea(5, 0), 0)

    def test_square_area_boundary(self):
        self.assertEqual(squareArea(0), 0)

    def test_triangle_area_boundary(self):
        self.assertEqual(traingleArea(0, 5), 0)
        self.assertEqual(traingleArea(5, 0), 0)

    '''Тесты на исключения'''

    def test_circle_area_exception(self):
        with self.assertRaises(TypeError):
            circleArea("string")

    def test_rectangle_area_exception(self):
        with self.assertRaises(TypeError):
            rectangleArea("a", 5)

    def test_square_area_exception(self):
        with self.assertRaises(TypeError):
            squareArea(None)

    def test_triangle_area_exception(self):
        with self.assertRaises(TypeError):
            traingleArea(3, "height")

    def test_triangle_perimeter_exception(self):
        with self.assertRaises(TypeError):
            trainglePerimeter(3, "side", 5)


if __name__ == "__main__":
    unittest.main()
