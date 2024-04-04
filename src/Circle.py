from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        self.area = math.pi * math.sqrt(self.radius)
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter
