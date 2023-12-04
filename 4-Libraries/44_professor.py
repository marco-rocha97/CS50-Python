# In a file called professor.py, implement a program that:

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
import random


def main():
    min, max = get_level()
    i = 0
    score = 0

    while i < 10:
        x, y = generate_integer(min, max)

        eq = x + y

        while True:
            try:
                ans = int(input(f"{x} + {y} = "))

                if eq == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    j = 0

                    while j < 2:
                        try:
                            ans = int(input(f"{x} + {y} = "))
                            if ans == eq:
                                break
                            else:
                                print("EEE")

                            j +=1

                        except:
                            pass

                    print(f"{x} + {y} = {eq}")
                    break

            except:
                pass

        i += 1

    print(f"Score: {score}")

def get_level():
    while True:

        try:
            n = int(input("Level: "))

            if n in [1,2,3]:

                if n == 1:
                    return 0, 9
                elif n == 2:
                    return 10, 99
                else:
                    return 100, 999

        except:
            pass


def generate_integer(min, max):
        x = random.randint(min, max)
        y = random.randint(min, max)

        return x, y


if __name__ == "__main__":
    main()