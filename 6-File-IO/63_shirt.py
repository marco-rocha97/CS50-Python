# In a file called shirt.py, implement a program that expects exactly two command-line arguments:

# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

# Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

# The program should instead exit via sys.exit:

# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.
# Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
import sys
from PIL import Image, ImageOps


def main():
    check_command_line()
    try:
        # open input (muppet)
        imagefile = Image.open(sys.argv[1])
    except(FileNotFoundError):
        sys.exit("Input does not exist")

    # resize and crop input (muppet)
    cs50_shirt = Image.open("shirt.png")
    new_imagefile = ImageOps.fit(imagefile, cs50_shirt.size)
    # overlay
    new_imagefile.paste(cs50_shirt, cs50_shirt)
    # save
    new_imagefile.save(sys.argv[2])


def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_1 = sys.argv[1].lower().split(".")
    file_2 = sys.argv[2].lower().split(".")

    check_extension(file_1[1])
    check_extension(file_2[1])
    check_same_extensions(file_1[1], file_2[1])


def check_extension(file):
    if file not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid input")


def check_same_extensions(file_1, file_2):
    if file_1 != file_2:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()