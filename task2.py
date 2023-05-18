def main(x):
    if x < 173:
        return 46 * ((0.03 - 83 * (x ** 3)) ** 6)
    if 173 <= x < 234:
        return (1 + x ** 3 + 10 * x) ** 4 - (x ** 3) / 40 - 36 * (x ** 7)
    if 234 <= x < 319:
        return x - 71 * (x ** 7)
    if x >= 319:
        return 19 * (x ** 3) + 1 + (x ** 7)


print(main(275))
print(main(197))
print(main(133))
print(main(306))
print(main(274))
