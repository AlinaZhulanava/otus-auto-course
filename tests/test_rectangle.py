from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle


def test_rectangle_creation():
    rectangle = Rectangle(8, 3)
    assert rectangle is not None and isinstance(rectangle, Figure)


def test_rectangle_creation_negative():
    rectangle = Rectangle(0, 0)
    assert ValueError
    rectangle = Rectangle(-4, 5)
    assert ValueError
    rectangle = Rectangle(4, -5)
    assert ValueError


def test_rectangle_area():
    rectangle = Rectangle(8, 3)
    assert rectangle.get_area() == 24


def test_rectangle_perimeter():
    rectangle = Rectangle(8, 3)
    assert rectangle.get_perimeter() == 22


def test_rectangle_add_area():
    rectangle = Rectangle(5, 2)
    rectangle.get_area()
    figure = Figure()
    assert rectangle.add_area(figure) == rectangle.area
    rectangle1 = Rectangle(4, 3)
    rectangle1.get_area()
    assert rectangle.add_area(rectangle1) == 22
    square = Square(5)
    square.get_area()
    assert rectangle.add_area(square) == 35
    triangle = Triangle(6, 8, 10)
    triangle.get_area()
    assert rectangle.add_area(triangle) == 10 + triangle.area
    circle = Circle(3)
    circle.get_area()
    assert rectangle.add_area(circle) == 10 + circle.area
