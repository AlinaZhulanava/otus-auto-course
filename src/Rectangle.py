from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        try:
            side_a > 0 and side_b > 0
        except:
            raise ValueError("Can't create rectangle with negative or 0 side")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        self.area = self.side_a * self.side_b
        return self.area

    def get_perimeter(self):
        self.perimeter = (self.side_a + self.side_b) * 2
        return self.perimeter
