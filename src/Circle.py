from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        try:
            radius > 0
        except:
            raise ValueError("Can't create a circle with negative or 0 side")
        self.radius = radius

    def get_area(self):
        self.area = math.pi * self.radius * self.radius
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter
