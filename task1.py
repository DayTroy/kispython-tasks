# Task 1
import math


def main(x, z, y):
    a = (74*(20*x**3+y**2)-66*(math.ceil(25*z-58*z**2-y**3))**5)
    b = (12 * z ** 5 + (y ** 3 + 99 * x ** 2 + z) ** 6)
    c = (24 * (x ** 2 + 53) ** 3 - (39 * y - 4 * z ** 2 - 1) ** 4)
    d = (math.log(38 * y ** 2 - 22 * x, 10) ** 4 - 39 * z ** 2)
    return (a / b) + (c / d)


print(main(-0.26, -0.3, 0.85))
print(main(-0.36, 0.22, 0.9))
print(main(-0.85, 0.5, -0.41))
print(main(-0.77, -0.6, 0.8))
print(main(-0.45, -0.43, -0.0))
print(main(-0.14, -0.3, -0.79))
