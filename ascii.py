# -*- coding: utf-8 -*-
from PIL import Image
import argparse

# First, build a command line input handler the ArgumentParser instance.
parser = argparse.ArgumentParser()

# Define the width and height of the input file, output file, and output character
parser.add_argument('file')     #Input File
parser.add_argument('-o', '--output')   #Output File
parser.add_argument('--width', type = int, default = 80) #Output character width
parser.add_argument('--height', type = int, default = 80) #Output character height

# Parse and get parameters
args = parser.parse_args()

# Input image file path
IMG = args.file

# Output character width
WIDTH = args.width

# Output character height
HEIGHT = args.height

# Output path
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):

    # Judge alpha value
    if alpha == 0:
        return ' '

    # Get the length of the character set, here is 70
    length = len(ascii_char)

    # Convert RGB values to grayscale gray, with grayscale values ranging from 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # Gray value range is 0-255, while character set is only 70
    # Need to do the following to map the gray value to the specified character
    unit = (256.0 + 1)/length

    # Returns the character corresponding to the gray value
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    # Open and adjust the width and height of the image
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    # Initialize the output string
    txt = ""

    # Traverse each line in the picture
    for i in range(HEIGHT):
        # Traversing each column in the row
        for j in range(WIDTH):
            # Convert RGB pixels of (j,i) coordinates to characters and add them to txt string
            txt += get_char(*im.getpixel((j,i)))
        # Need to add a newline after traversing a line
        txt += '\n'
    # Print to screen
    print(txt)

    # Output to file
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
