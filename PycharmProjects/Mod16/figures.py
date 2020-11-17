class Figures:
    pass

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # def get_x(self):
    #     return self.x
    #
    # def get_y(self):
    #     return self.y
    #
    # def get_width(self):
    #     return self.width
    #
    # def get_height(self):
    #     return self.height

    def get_attr(self):
        return self.x, self.y, self.width, self.height

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area_rect(self):
        return self.width * self.height

class Square:
    def __init__(self, a):
        self.a = a

    def get_side(self):
        return self.a

    def set_side(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def get_radius(self):
        return self.r

    def set_radius(self, r):
        self.r = r

    def get_area_circle(self):
        return 3.14 * self.r ** 2
