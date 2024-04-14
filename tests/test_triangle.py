import pytest

from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle


def test_triangle_creation():
    triangle = Triangle(6, 8, 10)
    assert triangle is not None and isinstance(triangle, Figure)


def test_triangle_creation_negative():
    with pytest.raises(ValueError, match=r"Can't create a triangle with such sides"):
        triangle = Triangle(20, 8, 10)
    with pytest.raises(ValueError, match=r"Can't create a triangle with such sides"):
        triangle = Triangle(0, 0, 0)
    with pytest.raises(ValueError, match=r"Can't create a triangle with such sides"):
        triangle = Triangle(-6, 8, 10)


def test_figure_get_area():
    triangle = Triangle(6, 8, 10)
    assert triangle.get_area() == 24


def test_figure_get_perimeter():
    triangle = Triangle(6, 8, 10)
    assert triangle.get_perimeter() == 24


def test_triangle_add_area():
    triangle = Triangle(12, 8, 10)
    triangle.get_area()
    figure = Figure()
    figure.get_area()
    assert triangle.add_area(figure) == triangle.area
    rectangle = Rectangle(2, 5)
    rectangle.get_area()
    assert triangle.add_area(rectangle) == triangle.area + rectangle.area
    square = Square(5)
    square.get_area()
    assert triangle.add_area(square) == triangle.area + square.area
    triangle1 = Triangle(6, 8, 10)
    triangle1.get_area()
    assert triangle.add_area(triangle1) == triangle.area + triangle1.area
    circle = Circle(3)
    circle.get_area()
    assert triangle.add_area(circle) == triangle.area + circle.area
