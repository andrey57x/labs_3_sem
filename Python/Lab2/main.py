from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np

def start():
    rect = Rectangle(22, 22, (0, 0, 255))
    circle = Circle(22, (0, 255, 0))
    square = Square(22, (255, 0, 0))
    arr = np.array([1, 2, 3])
    print(arr)
    print(rect.repr())
    print(circle.repr())
    print(square.repr())

if __name__ == "__main__":
    start()

