"""
Xinghua Wei A00978597
COMP 8505 Assignment 2
Staganography 
"""

#add zero to a binary number to match length
def add_zero(binary_num, expected_length):
    length = len(binary_num)
    return (expected_length-length) * '0' + binary_num

#convert decimal numbers representing RGB values of 
# a pixel into binary numbers of same value
def rgb_to_binary(r,g,b):
    return add_zero(bin(r)[2:],8), add_zero(bin(g)[2:],8), add_zero(bin(b)[2:],8)

#convert password to binary
def pwd_to_binary(password):
    b_password = bin(password)
    return b_password

#Ceaser cipher
def ceaser_enc(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char)+ 5-65)%26 +65)
        else:
            result += chr((ord(char)+ 5- 97)%26 + 97)
    return result

#decode ceaser cipher
def decode_cipher(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char)- 5-65)%26 +65)
        else:
            result += chr((ord(char) - 5- 97)%26 + 97)
    return result

def swap_cipher(binary_value):
    len_value = len(binary_value)
    swap_value = binary_value[len_value//2: len_value] + binary_value[0:len_value//2]
    return swap_value  
