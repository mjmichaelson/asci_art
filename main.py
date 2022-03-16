import sys
from PIL import Image
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

IMG_SHRINK_FACTOR = 2
MAX_PIXEL_VALUE = 255
ASCII_BRIGHTNESS_MAP_raw = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ASCII_BRIGHTNESS_MAP = sorted(enumerate(ASCII_BRIGHTNESS_MAP_raw))
ASCII_BRIGHTNESS_MAP.reverse()


# provides three possible methods, with default 'average'
def convert_rgb_pixel_to_brightness(p: tuple, method: str) -> int:
    if method == 'average':
        return int((p[0] + p[1] + p[2]) // 3)
    elif method == 'luminosity':
        return int((0.21 * p[0]) + (0.72 * p[1]) + (0.07 * p[2]))
    elif method == 'lightness':
        return int(max(p[0], p[1], p[2]) + min(p[0], p[1], p[2]) // 2)
    else:
        # default is average
        return int((p[0] + p[1] + p[2]) // 3)


def convert_brightness_to_ascii(b: int) -> str:
    # scale factor should be slightly higher than the actual divisor, to ensure no
    # resulting numbers are too large
    scale_factor = round((MAX_PIXEL_VALUE / len(ASCII_BRIGHTNESS_MAP) + 0.01), 2)

    # we pull out the value at the correct key
    raw_key = int(b // scale_factor)
    if raw_key > 65: raw_key = 65
    if raw_key < 0: raw_key = 0
    key = raw_key

    a = ASCII_BRIGHTNESS_MAP[key][1]
    return a


# takes flat list of RGB pixels
def construct_pixel_matrix(data: list, height: int, width: int) -> list[list]:
    pixel_matrix = [[] for row in range(height)]
    i = 0
    for r in range(height):
        for c in range(width):
            pixel_matrix[r].append(data[i])
            i += 1
    return pixel_matrix


# takes flat list of RGB pixels
def construct_brightness_matrix(data: list, height: int, width: int) -> list[list]:
    brightness_matrix = [[] for row in range(height)]
    i = 0
    for r in range(height):
        for c in range(width):
            p = convert_rgb_pixel_to_brightness(data[i], 'average')
            brightness_matrix[r].append(p)
            i += 1
    return brightness_matrix


def normalize_brightness_matrix(brightness_matrix: list[list]) -> list[list]:
    normalized_brightness_matrix = []
    max_pixel = max(map(max, brightness_matrix))
    min_pixel = min(map(min, brightness_matrix))
    for row in brightness_matrix:
        rescaled_row = []
        for p in row:
            r = MAX_PIXEL_VALUE * (p - min_pixel) / float(max_pixel - min_pixel)
            rescaled_row.append(r)
        normalized_brightness_matrix.append(rescaled_row)

    return normalized_brightness_matrix


def convert_brightness_mat_to_ascii_mat(brightness_matrix: list[list]) -> list[list]:
    ascii_matrix = [[] for r in range(len(brightness_matrix))]
    for i in range(len(brightness_matrix)):
        for j in brightness_matrix[i]:
            ascii_pixel = convert_brightness_to_ascii(j)
            ascii_matrix[i].append(ascii_pixel)
    return ascii_matrix


def print_ascii_matrix(mat: list[list]) -> None:
    for i in mat:
        for j in i:
            # print 3 times to counteract 'squashing' that results from
            # conversion of a square pixel to a rectangular ascii char
            print(j, j, j, sep='', end='')
        print('/n')


def main():
    # PART 1: load the image
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    if filename == '':
        # default is the ol' pineapple
        filename = 'ascii-pineapple.jpeg'
    im = Image.open(filename)

    # resize so that it will fit in terminal window
    shrink_factor = IMG_SHRINK_FACTOR
    im = im.resize((im.size[0] // shrink_factor, im.size[1] // shrink_factor))
    width, height = im.size
    data = [im.getdata()][0]

    # PART 2: load pixels into matrix
    # by-hand method
    # data_list = [im.getdata()]
    # pixel_matrix = [[] for row in range(height)]
    # i = 0
    # for r in range(height):
    #     for c in range(width):
    #         pixel_matrix[r].append(data_list[0][i])
    #         i += 1
    # Alternative: numpy reshape method
    # d = np.reshape(np.array(im.getdata()), (height, width, 3))

    # PART 3: convert to brightness matrix
    try:
        brightness_matrix = construct_brightness_matrix(data, height, width)

        # now still want to normalize values
        brightness_matrix = normalize_brightness_matrix(brightness_matrix)
    except:
        print(f'Oops! Attempting to construct '
              f'brightness matrix but {sys.exc_info()[0]} occurred.')
    else:
        print('Brightness matrix constructed successfully!')
        # print(f'size: {len(brightness_matrix)} x {len(brightness_matrix[0])}')

    # PART 4: Construct ASCII Matrix
    try:
        ascii_matrix = convert_brightness_mat_to_ascii_mat(brightness_matrix)
    except:
        print(f'Oops! Attempting to construct '
              f'ASCII matrix but {sys.exc_info()[0]} occurred.')
    else:
        print(f'Success! Made an ASCII matrix!')
        print_ascii_matrix(ascii_matrix)


if __name__ == '__main__':
    main()
