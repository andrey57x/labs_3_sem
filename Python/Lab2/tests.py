import unittest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class MyTestCase(unittest.TestCase):
    def test_rect(self):
        rect = Rectangle(5, 10, (0, 0, 255))
        self.assertEqual(rect.area(), 50)

    def test_square(self):
        square = Square(10, (255, 0, 0))
        self.assertEqual(square.area(), 100)

    def test_circle(self):
        circle = Circle(22, (0, 255, 0))
        self.assertEqual(circle.area(), math.pi * 22 ** 2)


if __name__ == '__main__':
    unittest.main()
