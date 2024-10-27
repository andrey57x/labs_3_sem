class Color:
    def __init__(self):
        self.__color = None

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value

    def del_color(self):
        del self.__color

    color = property(get_color, set_color, del_color)
