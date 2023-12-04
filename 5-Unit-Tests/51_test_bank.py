# In a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests
from bank import value


def main ():
    test_zero()
    test_twenty()
    test_hundred()


def test_zero():
    assert value("hello Marco") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_twenty():
    assert value("hi") == 20
    assert value("Hi Marco") == 20
    assert value("HOLA") == 20


def test_hundred():
    assert value("What's up?") == 100
    assert value("Good Morning") == 100
    assert value("Don't talk to me today") == 100


if __name__ == "__main__":
    main()