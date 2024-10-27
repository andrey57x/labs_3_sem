from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    def __init__(self, w: float, h: float, c: tuple[int, int, int]):
        self.width = w
        self.height = h
        self.name = "Rectangle"
        self.color = Color()
        self.color.color = c

    def area(self):
        return self.width * self.height

    def repr(self):
        return "{0} x {1} = {2}, {3}".format(self.width, self.height, self.area(), self.color.color)

    def get_name(self):
        return self.name
