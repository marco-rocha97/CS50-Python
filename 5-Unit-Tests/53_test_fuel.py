# In a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests
from fuel import convert, gauge
import pytest

def main():
    test_correct_inputs()
    test_zero_division()
    test_incorrect_inputs()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_incorrect_inputs():
    with pytest.raises(ValueError):
        convert("1/cat")
        convert("cat/2")
        convert("3/2")
        convert("-1/2")
        convert("1/-2")

def test_correct_inputs():
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("99/100") == 99 and gauge(99) == "F"


if __name__ == "__main__":
    main()