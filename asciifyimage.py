import cv2
import time
import numpy as np
import os
import math
import sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# print(color.BOLD + 'Hello World !' + color.END)

def asciify(img, out_width = 64):
    # convert image to greyscale format
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


    # resize the image
    height, width = img.shape
    # print(img.shape)
    aspect_ratio = width/height
    new_width = out_width
    new_height = int(new_width/aspect_ratio*.55)
    img = cv2.resize(img, (new_width, new_height))

    # reshape image into row vector
    flatImg = np.reshape(img, -1)

    # replace each pixel with a character from array
    # chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    # chars = "$@B%8WM#**oahkbpqmZO0QLJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`'."
    # chars = "$@B%8WM#**oahkbpqmZO0QLJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`'."
    # chars = "#."
    # chars = "█#."
    chars = "█▓▒░ "
    repeatN = math.ceil(255/len(chars))+1
    chars = "".join([x*repeatN for x in chars])

    new_pixels = [chars[pixel] for pixel in flatImg]
    # new_pixels = [chars[pixel//25] for pixel in flatImg]
    rows = ["".join(new_pixels[x*new_width:(x+1)*new_width]) for x in range(len(img))]
    finalImg = "\n".join(rows)

    return finalImg

