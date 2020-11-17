from figures import Rectangle, Square, Circle

rect_1 = Rectangle(5, 10, 50, 100)

print('Начальная точка, ширина и высота прямоугольника =', rect_1.get_attr())
print('Площадь прямоугольника =', rect_1.get_area_rect())
print('Rectangle', rect_1.get_attr(), sep='')

square_1 = Square(8)

print('Длина стороны квадрата =', square_1.get_side())
print('Площадь квадрата =', square_1.get_area_square())

circle_1 = Circle(4)

print('Радиус круга =', circle_1.get_radius())
print('Площадь круга =', circle_1.get_area_circle())
