# In a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests
from plates import is_valid


def main ():
    test_start_2_letters()
    test_len()
    test_straight()
    test_numbers()


def test_start_2_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False


def test_len():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") == False


def test_straight():
    assert is_valid("AAA") == True
    assert is_valid("AA A") == False
    assert is_valid("AAA.A") == False
    assert is_valid("AA?AA") == False
    assert is_valid("A!AAA") == False

def test_numbers():
    assert is_valid("AAA111") == True
    assert is_valid("AAA11A") == False
    assert is_valid("AAA10") == True
    assert is_valid("AAA01") == False


if __name__ == "__main__":
    main()