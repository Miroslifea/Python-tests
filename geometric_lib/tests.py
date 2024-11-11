import unittest
import math
from GeometricFunctions import *

class TestGeometryFunctions(unittest.TestCase):

    def test_circleArea(self):
        self.assertAlmostEqual(circleArea(1), math.pi)
        self.assertAlmostEqual(circleArea(0), 0)
        self.assertAlmostEqual(circleArea(2), math.pi * 4)

    def test_circlePerimeter(self):
        self.assertAlmostEqual(circlePerimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circlePerimeter(0), 0)
        self.assertAlmostEqual(circlePerimeter(2), 4 * math.pi)

    def test_rectangleArea(self):
        self.assertEqual(rectangleArea(2, 3), 6)
        self.assertEqual(rectangleArea(0, 3), 0)
        self.assertEqual(rectangleArea(4, 5), 20)

    def test_rectanglePerimeter(self):
        self.assertEqual(rectanglePerimeter(2, 3), 10)
        self.assertEqual(rectanglePerimeter(0, 3), 6)
        self.assertEqual(rectanglePerimeter(4, 5), 18)

    def test_squareArea(self):
        self.assertEqual(squareArea(2), 4)
        self.assertEqual(squareArea(0), 0)
        self.assertEqual(squareArea(5), 25)

    def test_squarePerimeter(self):
        self.assertEqual(squarePerimeter(2), 8)
        self.assertEqual(squarePerimeter(0), 0)
        self.assertEqual(squarePerimeter(5), 20)

    def test_traingleArea(self):
        self.assertEqual(traingleArea(2, 3), 3)
        self.assertEqual(traingleArea(0, 3), 0)
        self.assertEqual(traingleArea(4, 5), 10)

    def test_trainglePerimeter(self):
        self.assertEqual(trainglePerimeter(3, 4, 5), 12)
        self.assertEqual(trainglePerimeter(0, 0, 0), 0)
        self.assertEqual(trainglePerimeter(5, 5, 5), 15)

if __name__ == '__main__':
    unittest.main()
