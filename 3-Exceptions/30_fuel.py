# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
while True:
    fuel = input("Fraction: ")

    try:
        x, y = fuel.split("/")

        if x.isnumeric() and y.isnumeric():
            x = int(x)
            y = int(y)

            f = round(100*x/y, 0)

            if x <= y:
                if f <= 1:
                    print("E")
                elif f < 99:
                    print(f"{int(f)}%")
                else:
                    print("F")
                break

    except(ValueError, ZeroDivisionError):
        pass