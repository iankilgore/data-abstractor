# data-abstractor

Here is an overview of how these various python scripts work, and how to use them.

# Audio spectrogram generator
Files: "audio-spectro.py", "audio-spectro-no-display.py"\
This tool can take an audio file and output a frequency graph, which will show the different frequencies in the file, and plots it on a spectrogram. The recommended maximum length of audio files is 90 seconds. If your files are any longer than that, python may crash due to memory allocation errors, even in systems with sufficent RAM. It works with systems that have at least 16GB RAM (you could maybe use a system with less, although I haven't tested that).\
The difference between "audio-spectro.py" and "audio-spectro-no-display.py" is that the first one will pop up a preview window for what the spectrogram looks like (assuming you are running a system with a GUI), while the "no-display" one does not do this.

# Average RGB Color generation
Files: "average-color-image.py", "average-color-video-frames-multicore.py", "average-color-video-frames.py"\
These tools can take and image file or video file, and it will output the RGB values after it determines the average color and outputs it to the terminal, it works by adding up all the pixel values, then dividing by the number of pixels.\
"averge-color-image.py" is for image files, "average-color-video-frames.py" is for video files, and it will output the average RGB value to the terminal, frame by frame. "average-color-video-frames-multicore.py" is also for video files, however the difference is that it uses all the CPU cores instead of just one, and therefore will reduce the amount of time spent waiting for the process to finish.\

# Duplicate Line finder
Files: "duplicate-line-finder.py"\
*This tool is still currently under development*\
This tool will allow the user to scan files for duplicate lines in a text file, in other words, if the characters match on two different lines, it outputs that result.

# Video Text Extraction
Files: "extract-video-text.py"\
This tool is dependent on the tesseract tool, which can be downloaded here (for Windows): https://github.com/UB-Mannheim/tesseract/wiki, or if you are using Ubuntu Linux, you can use "sudo apt-get install tesseract-ocr" \
This tool allows the user to scan video files for text. Accuracy can vary, and is usually not 100% accurate, human verification is recommended to ensure the result is correct. It works best with screen recordings, where the screen was recorded directly on the computer, as opposed to videoing the screen or a piece of paper. The clearer the text in the video file is, the higher the accuracy will be.

# Video/Image to ASCII converter
Files: "image2ascii.py", "video2ascii.py", "video2ascii-4x-size.py", "video2ascii-16x-size.py"
These tools take an image or video file and makes ASCII art with it, the "image2ascii.py" converts an image file to ASCII, and the "video2ascii.py" take a video file and outputs a text file for each video frame. \
The 4x-size and 16x-size also is for video files, these can be used if you would like to preserve more close-up detail in the video, however, the larger sizes generally are not practical, since many computer screens are not large enough, and will crop off the characters after a certain point. 

