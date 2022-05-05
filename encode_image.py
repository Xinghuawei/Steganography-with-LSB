from PIL import Image
from helper import add_zero, rgb_to_binary, swap_cipher

"""
Xinghua Wei A00978597
COMP 8505 Assignment 2
Staganography 
"""

#get binary format of RGB values of an image
def get_pixel_binary_value(img, width, height):
    hidden_image_pixels=''
    for col in range(width):
        for row in range(height):
            singal_pixel = img[col, row]
            r = singal_pixel[0]
            g = singal_pixel[1]
            b = singal_pixel[2]
            r_binary, g_binary, b_binary = rgb_to_binary(r,g,b)
            hidden_image_pixels += r_binary + g_binary + b_binary
    #apply swap cipher to pixels
    swap_cipher(hidden_image_pixels)
    return hidden_image_pixels

#Replaces the 1 least significant bits of a subset of pixels 
# in an image with binary bit representing a image be hidden.
#first pixel at top left is to store width and height
def modify_binary_value(img_carrier, width_carrier, height_carrier, width_hidden, height_hidden,hidden_image_pixels ):
    index = 0
    for col in range(width_carrier):
        for row in range(height_carrier):
            if row == 0 and col == 0:
                #add zero to match length
                width_hidden_binary = add_zero(bin(width_hidden)[2:],12)
                height_hidden_binary = add_zero(bin(height_hidden)[2:],12)
                total_size_binary = width_hidden_binary + height_hidden_binary
                img_carrier[col,row] = (int(total_size_binary[0:8],2),int(total_size_binary[8:16],2),
                int(total_size_binary[16:24],2))
                continue
            r, g, b = img_carrier[col, row]
            r_binary, g_binary, b_binary = rgb_to_binary(r,g,b)
            r_binary = r_binary[0:7] + hidden_image_pixels[index:index+1]
            g_binary = g_binary[0:7] + hidden_image_pixels[index+1:index+2]
            b_binary = b_binary[0:7] + hidden_image_pixels[index+2:index+3]
            index+=3
            img_carrier[col,row] = (int(r_binary,2), int(g_binary,2), int(b_binary,2))
            if index >= len(hidden_image_pixels):
                return img_carrier
    return img_carrier

#call above functions
def encode_image(img_carrier, img_hidden):
    encoded_image = img_carrier.load()
    img_hidden_copy = img_hidden.load()
    width_carrier, height_carrier=img_carrier.size
    width_hidden, height_hidden=img_hidden.size
    hidden_image_pixels = get_pixel_binary_value(img_hidden_copy,width_hidden,height_hidden)
    encoded_image = modify_binary_value(encoded_image,width_carrier,height_carrier,width_hidden,height_hidden,hidden_image_pixels)
    return img_carrier


