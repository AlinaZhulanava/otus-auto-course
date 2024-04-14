import pytest

from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle


def test_figure_creation():
    figure = Figure()
    assert figure is not None


def test_figure_get_area():
    figure = Figure()
    assert figure.get_area() == 0


def test_figure_get_perimeter():
    figure = Figure()
    assert figure.get_perimeter() == 0


def test_figure_add_area():
    figure = Figure()
    assert figure.add_area(figure) == 0
    rectangle = Rectangle(5, 2)
    rectangle.get_area()
    assert figure.add_area(rectangle) == rectangle.area
    square = Square(5)
    square.get_area()
    assert figure.add_area(square) == 25
    triangle = Triangle(6, 8, 10)
    triangle.get_area()
    assert figure.add_area(triangle) == triangle.area
    circle = Circle(3)
    circle.get_area()
    assert figure.add_area(circle) == circle.area

    def test_figure_add_area_negative():
        figure = Figure()
        rectangle = Rectangle(5, 2)
        triangle = Triangle(5, 8, 6)
        square = Square(5)
        circle = Circle(3)
        for object in [figure, triangle, rectangle, square, circle]:
            object.get_area()
            with pytest.raises(ValueError, match=r"The second object isn't a figure"):
                for not_figure_element in [11, 11.99, "abc", None, Figure]:
                    object.add_area(not_figure_element)
