from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if (side_a < side_b + side_c and
                side_b < side_a + side_c and
                side_c < side_a + side_b):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise ValueError("Can't create a triangle with such sides")

    def get_area(self):
        p = self.get_perimeter() / 2
        self.area = math.sqrt(p * (p - self.side_a) *
                              (p - self.side_b) * (p - self.side_c))
        return self.area

    def get_perimeter(self):
        self.perimeter = self.side_a + self.side_b + self.side_c
        return self.perimeter
