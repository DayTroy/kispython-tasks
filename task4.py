def main(n):
    if n == 0:
        return -0.24
    if n == 1:
        return 0.60
    if n >= 2:
        return 15 * main(n - 2) ** 3 + 0.02 + main(n - 1)


print(main(6))
print(main(4))
print(main(3))
print(main(7))
print(main(5))
