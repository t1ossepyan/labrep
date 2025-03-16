class Shape:
    def __init__(self, len, width):
        self.len = len
        self.width = width
    
class Rectangle(Shape):
    def computeArea(self):
        print(self.len * self.width)

figure = Rectangle(34, 43)

figure.computeArea()
