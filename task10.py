class Mealy:
    def __init__(self):
        self.state = "A"

    def load(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 2
        if self.state == "D":
            return 5
        if self.state == "F":
            self.state = "D"
            return 8
        raise MealyError("load")

    def punch(self):
        if self.state == "D":
            self.state = "E"
            return 4
        if self.state == "E":
            self.state = "F"
            return 6
        if self.state == "F":
            self.state = "G"
            return 7
        raise MealyError("punch")

    def tread(self):
        if self.state == "C":
            self.state = "F"
            return 3
        if self.state == "F":
            self.state = "A"
            return 9
        raise MealyError("tread")


class MealyError(Exception):
    pass


def main():
    return Mealy()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.load() == 2
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.punch() == 7
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.load() == 2
    assert o.load() == 5
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.load() == 8
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.punch() == 7
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.tread() == 3
    assert o.punch() == 7
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.tread() == 3
    assert o.load() == 8
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.punch() == 7
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.tread() == 3
    assert o.tread() == 9
    assert o.load() == 0
    assert o.load() == 1
    assert o.tread() == 3
    assert o.punch() == 7
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.tread() == 3
    assert o.tread() == 9
    assert o.load() == 0
    assert o.load() == 1
    assert o.load() == 2
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.punch() == 7
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.tread() == 3
    assert o.tread() == 9
    assert o.load() == 0
    assert o.load() == 1
    assert o.load() == 2
    assert o.load() == 5
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.punch() == 7
    o = main()
    assert o.load() == 0
    assert o.load() == 1
    assert o.tread() == 3
    assert o.tread() == 9
    assert o.load() == 0
    assert o.load() == 1
    assert o.load() == 2
    assert o.load() == 5
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.load() == 8
    assert o.punch() == 4
    assert o.punch() == 6
    assert o.punch() == 7
    raises(lambda: o.punch(), MealyError)
    o = main()
    raises(lambda: o.tread(), MealyError)
    assert o.load() == 0
    raises(lambda: o.punch(), MealyError)


test()
