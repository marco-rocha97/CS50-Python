# n a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
def main():
    new_time = convert(input("Time: "))

    if 7 <= new_time <= 8:
        print("breakfast time")
    elif 12<= new_time <= 13:
        print("lunch time")
    elif 18<= new_time <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    decimal = float(h) + float(m)/60
    print(decimal)
    return decimal


if __name__ == "__main__":
    main()