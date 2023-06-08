def top(tree):
    if tree[3] == 1970:
        if tree[0] == "TEX":
            return 0
        if tree[0] == "MAKO":
            return 1
    if tree[3] == 2013:
        return 2
    if tree[3] == 1959:
        return 3


def middle(tree):
    if tree[3] == 1970:
        return 4
    if tree[3] == 2013:
        return 5
    if tree[3] == 1959:
        if tree[1] == "PERL6":
            return 6
        if tree[1] == "XSLT":
            return 7


def bottom(tree):
    if tree[0] == "TEX":
        return 8
    if tree[0] == "MAKO":
        return 9


def main(tree):
    if tree[2] == "M4":
        return top(tree)

    if tree[2] == "NINJA":
        return middle(tree)

    if tree[2] == "NGINX":
        return bottom(tree)


print(main(["TEX", "PERL6", "NINJA", 2013]))  # return 5
print(main(["TEX", "XSLT", "NINJA", 1970]))  # return 4
print(main(["TEX", "XSLT", "M4", 1959]))  # return 3
print(main(["TEX", "PERL6", "NGINX", 1959]))  # return 8
print(main(["TEX", "XSLT", "M4", 1970]))  # return 0
