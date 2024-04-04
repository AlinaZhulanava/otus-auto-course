class Figure:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.get_area()
        else:
            raise ValueError("The second object isn't a figure")
