import math


def main(y):
    n = len(y)
    count = 0
    y.insert(0, 0)
    for i in range(1, n + 1):
        count += (y[n + 1 - math.ceil(i / 4)]) ** 3 \
                 - 72 * (y[n + 1 - math.ceil(i / 4)]) ** 2 \
                 - y[n + 1 - math.ceil(i / 4)]
    return count


print(main([0.97, 0.62, -0.48, 0.89, 0.92, 0.89]))
