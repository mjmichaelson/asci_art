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

    # load pixels into matrix
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



if __name__ == '__main__':
    main()
