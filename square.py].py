class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, len, height):
        self.len = len
        self.height = height

    def area(self):
        return self.height * self.len


a = int(input())
b = int(input())
object = Square(a, b)

print(f"Длинна: {object.len}, Ширина: {object.height}", "Площадь", object.area())

