from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, s: float, c: tuple[int, int, int]):
        super().__init__(s, s, c)
        self.name = "Square"
