from PIL import Image
from helper import rgb_to_binary, swap_cipher

"""
Xinghua Wei A00978597
COMP 8505 Assignment 2
Staganography 
"""


def extract_hidden_pixel(image,width_carrier, height_carrier, count_pixel):
    hidden_image_pixels = ''
    index = 0

    for col in range(width_carrier):
        for row in range(height_carrier):
            if row == 0 and col == 0 :
                continue
            r, g, b = image[col, row]
            r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
            #hidden_image_pixels += r_binary + g_binary + b_binary
            hidden_image_pixels += r_binary[7:8] + g_binary[7:8] + b_binary[7:8]
            if index >= count_pixel * 2:
                return hidden_image_pixels
    #reverse cipher
    swap_cipher(hidden_image_pixels[24:])

    return hidden_image_pixels

def reconstruct_image(image_pixel, width, height):
    image = Image.new("RGB",(width,height))
    image_copy = image.load()
    index = 0
    for col in range(width):
        for row in range(height):
            r_binary = image_pixel[index:index+8]
            g_binary = image_pixel[index+8:index+16]
            b_binary = image_pixel[index+16:index+24]
            image_copy[col, row] = (int(r_binary,2), int(g_binary,2), int(b_binary,2))
            index+=24
    return image

def decode_image(image):
    image_copy = image.load()
    width_carrier, height_carrier = image.size
    r, g, b = image_copy[0,0]
    r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
    total_binary = r_binary + g_binary + b_binary
    width_hidden = int(total_binary[0:12], 2)
    height_hidden = int(total_binary[12:24], 2)
    count_pixel = width_hidden * height_hidden
    hidden_image_pixels = extract_hidden_pixel(image_copy, width_carrier, height_carrier, count_pixel)
    decoded_image = reconstruct_image(hidden_image_pixels, width_hidden, height_hidden)
    return decoded_image