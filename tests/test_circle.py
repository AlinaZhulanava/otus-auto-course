from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle
import math


def test_circle_creation():
    circle = Circle(5)
    assert circle is not None and isinstance(circle, Figure)


def test_circle_creation_negative():
    circle = Circle(0)
    assert ValueError
    circle = Circle(-1)
    assert ValueError


def test_circle_area():
    circle = Circle(3)
    assert circle.get_area() == math.pi * 9


def test_circle_perimeter():
    circle = Circle(3)
    assert circle.get_perimeter() == 6 * math.pi


def test_figure_add_area():
    circle = Circle(4)
    circle.get_area()
    figure = Figure()
    assert circle.add_area(figure) == circle.area
    rectangle = Rectangle(5, 2)
    rectangle.get_area()
    assert circle.add_area(rectangle) == circle.area + 10
    square = Square(5)
    square.get_area()
    assert circle.add_area(square) == 25 + circle.area
    triangle = Triangle(6, 8, 10)
    triangle.get_area()
    assert circle.add_area(triangle) == triangle.area + circle.area
    circle1 = Circle(3)
    circle.get_area()
    assert circle.add_area(circle1) == circle.area + circle1.area
