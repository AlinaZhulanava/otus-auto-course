from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a, side_a)

    def get_area(self):
        self.area = self.side_a ** 2
        return self.area