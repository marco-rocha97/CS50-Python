# In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        if matches := re.search(r"(?:(?:https?)+:\/\/(?:www\.)?youtube\.com\/embed\/)(\w+)", s):
            return "https://youtu.be/" + matches.group(1)
    else:
        return "None"


if __name__ == "__main__":
    main()