from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math


class Circle(Figure):
    def __init__(self, r: float, c: tuple[int, int, int]):
        self.radius = r
        self.name = "Circle"
        self.color = Color()
        self.color.color = c

    def area(self):
        return math.pi * self.radius ** 2

    def repr(self):
        return "pi x {0} ^ 2 = {1}, {2}".format(self.radius, self.area(), self.color.color)

    def get_name(self):
        return self.name
