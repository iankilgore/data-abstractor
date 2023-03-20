import cv2
import numpy as np
from multiprocessing import Pool, cpu_count

def average_frame_color(frame):
    height, width, _ = frame.shape
    pixels = frame.reshape(height * width, 3)

    r_sum = g_sum = b_sum = 0
    for pixel in pixels:
        b, g, r = pixel
        r_sum += r
        g_sum += g
        b_sum += b

    num_pixels = height * width
    avg_r = r_sum / num_pixels
    avg_g = g_sum / num_pixels
    avg_b = b_sum / num_pixels

    return (int(avg_b), int(avg_g), int(avg_r))

def process_frame(frame):
    return average_frame_color(frame)

if __name__ == '__main__':
    file_name = input("Enter the name of the video file (including the extension): ")
    cap = cv2.VideoCapture(file_name)

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    with Pool(cpu_count()) as p:
        results = p.map(process_frame, frames)

    for result in results:
        print(result)

    cap.release()
    cv2.destroyAllWindows()
