import sys
import os
import cv2
from PIL import Image
import io

# prompt the user for the input video filename
input_file = input("Enter the input video filename: ")

# prompt the user for the output directory name
output_dir = input("Enter the output directory name: ")

# create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# open the video file
video = cv2.VideoCapture(input_file)

# loop through each frame of the video
frame_count = 0
while True:
    # read the next frame from the video
    ret, frame = video.read()

    # if there are no more frames, break out of the loop
    if not ret:
        break

    # convert the frame to grayscale and resize it
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = frame.shape
    new_width = 1920

    # compute the aspect ratio of the original frame
    aspect_ratio = width / height

    # compute the new height of the resized frame
    new_height = int(new_width / aspect_ratio * 0.55)

    frame = cv2.resize(frame, (new_width, new_height))

    # create a PIL Image object from the frame
    img = Image.fromarray(frame)

    # create a memory buffer to hold the PNG image data
    buffer = io.BytesIO()

    # save the image to the memory buffer in PNG format
    img.save(buffer, format='PNG')

    # read the PNG image data from the memory buffer
    png_data = buffer.getvalue()

    # convert the PNG image data to ASCII art
    ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    im = Image.open(io.BytesIO(png_data))
    #im = im.transpose(Image.ROTATE_270)  # rotate the image by 90 degrees counterclockwise
    im = im.convert('L')
    pixels = list(im.getdata())
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])

    # split the characters into lines of the same width as the frame
    lines = [characters[i:i+new_width] for i in range(0, len(characters), new_width)]

    # save the ASCII art to a text file
    output_file = os.path.join(output_dir, f"frame{frame_count}.txt")
    with open(output_file, "w") as file:
        file.write('\n'.join(lines))

    frame_count += 1

# release the video file handle
video.release()
