import cv2
import subprocess

# Prompt user for input file name
input_file = input("Enter the name of the input video file: ")

# Prompt user for output file name
output_file = input("Enter the name of the output text file: ")

# Open the video file
video = cv2.VideoCapture(input_file)

# Initialize the output file
with open(output_file, 'w') as f:
    # Loop through each frame of the video
    while True:
        # Read the next frame
        ret, frame = video.read()

        # If there are no more frames, break the loop
        if not ret:
            break

        # Convert the frame to a grayscale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Encode the image to a memory buffer
        _, buffer = cv2.imencode('.png', gray)

        # Pass the memory buffer to tesseract
        process = subprocess.Popen(["tesseract", "stdin", "stdout"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, _ = process.communicate(buffer.tobytes())

        # Write the text to the output file
        f.write(stdout.decode('utf-8'))

# Release the video file
video.release()

print("Text extracted successfully!")