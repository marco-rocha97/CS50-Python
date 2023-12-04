# In a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests
from twttr import shorten


def main():
    test_word()


def test_word():
    assert shorten("marco") == "mrc"
    assert shorten("MARCO") == "MRC"
    assert shorten("MarcO") == "Mrc"


def test_number():
    assert shorten("1234") == "1234"


def test_punctuation():
    assert shorten(".,!?") == ".,!?"


if __name__ == "__main__":
    main()