# Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. 
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
import sys


def main():
    check_command_line_input()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except(FileNotFoundError):
        sys.exit("File does not exit")

    count = 0
    for line in lines:
        if check_comment_empty(line) == False:
            count += 1

    print(count)


def check_command_line_input():
    if len(sys.argv) == 2: # aqui também
        if (sys.argv[1][-3:]) != ".py": # aqui da pra melhorar, Marco
            sys.exit("Not a Python file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def check_comment_empty(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()