import sys
from PIL import Image

# prompt the user for the input image filename
input_file = input("Enter the input image filename: ")

# open the image file
image = Image.open(input_file)

# resize the image
width, height = image.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55 # 0.55 is the aspect ratio of one character

image = image.resize((new_width, int(new_height)))

# convert image to grayscale format
image = image.convert('L')

# define the ASCII characters to use
ASCII_CHARS = ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# convert each pixel to an ASCII character
pixels = image.getdata()
characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])

# split the characters into lines of the same width as the image
lines = [characters[i:i+new_width] for i in range(0, len(characters), new_width)]

# prompt the user for the output filename
output_file = input("Enter the output filename (default is ascii.txt): ") or "ascii.txt"

# save the ASCII art to a text file
with open(output_file, "w") as file:
    file.write('\n'.join(lines))
