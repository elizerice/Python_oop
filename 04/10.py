class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

  
    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
