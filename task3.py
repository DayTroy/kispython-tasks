import math


def main(m, z, n, y):
    sum1 = 0
    sum2 = 0
    for k in range(1, m + 1):
        sum1 += (math.exp((k ** 2) + z)) ** 5 + math.sin(k) / \
                72 + (math.ceil(z ** 2)) ** 4

    for k in range(1, n + 1):
        sum2 += 38 * (k ** 2 - 53 * y ** 3) ** 6
    return sum1 + sum2


print(main(4, 0.93, 7, 0.08))
print(main(8, 0.91, 3, 0.2))
print(main(2, -0.66, 5, 0.57))
print(main(7, 0.91, 3, -0.21))
print(main(4, -0.83, 3, -0.22))
