import unittest
from hw01_yu_zhou import classify_triangle


class TestTriangles(unittest.TestCase):
    def test_classify_triangles(self):
        with self.assertRaises(ValueError):
            classify_triangle(0, 1, 1)
        with self.assertRaises(ValueError):
            classify_triangle(2, -1, 3)
        with self.assertRaises(ValueError):
            classify_triangle(3, 1, -1)
        self.assertTrue(classify_triangle(3, 4, 5), 'right triangle')
        self.assertTrue(classify_triangle(3, 3, 3), 'equilateral triangle')
        self.assertTrue(classify_triangle(2, 3, 3), 'isosceles triangle')
        self.assertTrue(classify_triangle(1, 2, 3), 'it is not a triangle')
        self.assertTrue(classify_triangle(4, 5, 6), 'scalene triangle')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)