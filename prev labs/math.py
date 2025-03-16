import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degree: "))
radian = degree_to_radian(degree)
print(f"Output radian: {radian:.6f}")



def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = trapezoid_area(height, base1, base2)
print(f"Expected Output: {area}")


import math

def polygon_area(n, side_length):
    return (n * side_length**2) / (4 * math.tan(math.pi / n))

n = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = polygon_area(n, side_length)
print(f"The area of the polygon is: {area:.2f}")


def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base, height)
print(f"Expected Output: {area}")
