import sys
from PIL import Image
import numpy as np


def main():
    try:
        im = Image.open('ascii-pineapple.jpeg')
    except:
        print(f'Oops! Attempting to load image '
              f'but {sys.exc_info()[0]} occurred.')
    else:
        print('Image loaded successfully!')
        # print(f'{im.format}, {im.size}, {im.mode}')
        print(f'Image size: {im.size[0]} x {im.size[1]}')

    try:
        pixel_matrix = np.asarray(im)

        # Iterate though all pixels to test
        print(pixel_matrix)
    except:
        print(f'Oops! Attempting to construct '
              f'pixel matrix but {sys.exc_info()[0]} occurred.')
    else:
        print('Pixel matrix constructed successfully!')
        #print(f'Pixel matrix size: {imdata.size[0]} x {imdata.size[1]}')



if __name__ == '__main__':
    main()
