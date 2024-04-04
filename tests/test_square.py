from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle


def test_square_creation():
    square = Square(4)
    assert square is not None and isinstance(square, Figure)


def test_square_creation_negative():
    square = Square(0)
    assert ValueError
    square = Square(-4)
    assert ValueError


def test_square_area():
    square = Square(9)
    assert square.get_area() == 81


def test_square_perimeter():
    square = Square(7)
    assert square.get_perimeter() == 28


def test_square_add_area():
    square = Square(6)
    square.get_area()
    figure = Figure()
    assert square.add_area(figure) == 36
    rectangle = Rectangle(4, 3)
    rectangle.get_area()
    assert square.add_area(rectangle) == 48
    square1 = Square(5)
    square1.get_area()
    assert square.add_area(square1) == 61
    triangle = Triangle(6, 8, 10)
    triangle.get_area()
    assert square.add_area(triangle) == 36 + triangle.area
    circle = Circle(3)
    circle.get_area()
    assert square.add_area(circle) == 36 + circle.area
