# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

# usar sys para input
# 0 - random
if len(sys.argv) == 1:
    s = input("Input: ")
    f = random.choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(s))
# 2 - fonte especifica
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if sys.argv[2] in fonts:
        s = input("Input: ")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(s))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")