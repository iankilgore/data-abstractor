from PIL import Image

def average_image_color(image):
    width, height = image.size
    pixels = image.load()

    r_sum = g_sum = b_sum = 0
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r_sum += r
            g_sum += g
            b_sum += b

    num_pixels = width * height
    avg_r = r_sum / num_pixels
    avg_g = g_sum / num_pixels
    avg_b = b_sum / num_pixels

    return (int(avg_r), int(avg_g), int(avg_b))

file_name = input("Enter the name of the image file (including the extension): ")
image = Image.open(file_name)
average_color = average_image_color(image)
print(average_color)
