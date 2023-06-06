class Solver:
    def __init__(self):
        self.data = "A"

    def send(self):
        if self.data == "A":
            self.data = "B"
            return 0
        if self.data == "D":
            self.data = "B"
            return 4
        if self.data == "E":
            self.data = "F"
            return 5
        if self.data == "F":
            self.data = "G"
            return 6
        if self.data == "G":
            self.data = "E"
            return 8

        raise MealyError('send')

    def patch(self):
        if self.data == "B":
            self.data = "C"
            return 1
        if self.data == "C":
            self.data = "D"
            return 2
        if self.data == "D":
            self.data = "E"
            return 3
        if self.data == "F":
            self.data = "B"
            return 7
        if self.data == "G":
            self.data = "B"
            return 9
        raise MealyError('patch')


class MealyError(Exception):
    pass


def main():
    return Solver()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.send() == 0
    assert o.patch() == 1
    assert o.patch() == 2
    assert o.send() == 4
    o = main()
    assert o.send() == 0
    assert o.patch() == 1
    assert o.patch() == 2
    assert o.patch() == 3
    assert o.send() == 5
    assert o.patch() == 7
    o = main()
    assert o.send() == 0
    assert o.patch() == 1
    assert o.patch() == 2
    assert o.patch() == 3
    assert o.send() == 5
    assert o.send() == 6
    assert o.patch() == 9
    o = main()
    assert o.send() == 0
    assert o.patch() == 1
    assert o.patch() == 2
    assert o.patch() == 3
    assert o.send() == 5
    assert o.send() == 6
    assert o.send() == 8
    assert o.send() == 5
    assert o.patch() == 7

    raises(lambda: o.send(), MealyError)
    o = main()
    raises(lambda: o.patch(), MealyError)
    assert o.send() == 0
    raises(lambda: o.send(), MealyError)
