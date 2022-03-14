import sys
from PIL import Image
import numpy as np

_ASCII_BRIGHTNESS_MAP = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def convert_rgb_pixel_to_brightness(p):
    # average method
    return (p[0] + p[1] + p[2]) // 3


def convert_brightness_to_ascii(b):
    # scale factor should be slightly higher than the actual divisor, to ensure no
    # resulting numbers are too large
    scale_factor = round((255 / len(_ASCII_BRIGHTNESS_MAP) + 0.01), 2)
    return int(b // scale_factor)


def print_ascii_matrix(mat):
    for i in mat:
        for j in i:
            # print 3 times to counteract 'squashing' that results from
            # conversion of a square pixel to a rectangular ascii char
            print(j, sep='', end='')
            print(j, sep='', end='')
            print(j, sep='', end='')
        print('/n')


def main():
    # PART 1: load the image
    try:
        im = Image.open('ascii-pineapple.jpeg')
    except:
        print(f'Oops! Attempting to load image '
              f'but {sys.exc_info()[0]} occurred.')
    else:
        print('Image loaded successfully!')
        # print(f'{im.format}, {im.size}, {im.mode}')
        print(f'Image size: {im.size[0]} x {im.size[1]}')

    # PART 2: load pixels into matrix
    try:
        # by-hand method
        data_list = [im.getdata()]
        pixel_matrix = [[] for row in range(im.size[0])]
        i = 0
        for r in range(im.size[0]):
            for c in range(im.size[1]):
                pixel_matrix[r].append(data_list[0][i])
                i += 1

        # numpy reshape method
        d = np.reshape(np.array(im.getdata()), (im.size[0], im.size[1], 3))
        #print(d)
        #print(d.size)

        # Iterate though all pixels to test
        #print(pixel_matrix)
        #print(len(pixel_matrix), len(pixel_matrix[0]))

    except:
        print(f'Oops! Attempting to construct '
              f'pixel matrix but {sys.exc_info()[0]} occurred.')
    else:
        print('Pixel matrix constructed successfully!')
        #print(f'Pixel matrix size: {imdata.size[0]} x {imdata.size[1]}')

    # PART 3: convert to brightness matrix
    try:
        # by-hand method
        data_list = [im.getdata()]
        brightness_matrix = [[] for row in range(im.size[0])]
        i = 0
        for r in range(im.size[0]):
            for c in range(im.size[1]):
                p = convert_rgb_pixel_to_brightness(data_list[0][i])
                brightness_matrix[r].append(p)
                i += 1
    except:
        print(f'Oops! Attempting to construct '
              f'brightness matrix but {sys.exc_info()[0]} occurred.')
    else:
        print('Brightness matrix constructed successfully!')
        print(f'size: {len(brightness_matrix)} x {len(brightness_matrix[0])}')

    # PART 4: Construct ASCII Matrix
    try:
        ascii_matrix = [[] for r in range(len(brightness_matrix))]
        for i in range(len(brightness_matrix)):
            for j in brightness_matrix[i]:
                a = convert_brightness_to_ascii(j)
                ascii_pixel = _ASCII_BRIGHTNESS_MAP[a]
                ascii_matrix[i].append(ascii_pixel)
    except:
        print(f'Oops! Attempting to construct '
              f'ASCII matrix but {sys.exc_info()[0]} occurred.')
    else:
        print(f'Success! Made an ASCII matrix!')
        print(ascii_matrix)
        print_ascii_matrix(ascii_matrix)


if __name__ == '__main__':
    main()
