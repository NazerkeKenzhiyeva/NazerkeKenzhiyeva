import math

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = 0.25 * (sides * length**2) / (1 / math.tan(math.pi / sides))
print(f"The area of the polygon is: {area:.1f}")
