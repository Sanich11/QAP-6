class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_attr(self):
        return self.length, self.width

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def get_area_rect(self):
        return self.length * self.width
