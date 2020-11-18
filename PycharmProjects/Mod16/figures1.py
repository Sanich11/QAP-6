class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Rectangle(Figure):
    def __init__(self, color, width=10, height=5):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area_rect(self):
        return self.width * self.height


class Square(Figure):
    def __init__(self, color, a):
        super().__init__(color)
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle(Figure):
    def __init__(self, color, r):
        super().__init__(color)
        self.r = r

    def get_area_circle(self):
        return 3.14 * self.r ** 2


c = Circle('red', 5)
print(c.get_area_circle())
print(c.color)
