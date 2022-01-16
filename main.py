import sys
from PIL import Image

def main():
    try:
        im = Image.open("ascii-pineapple.jpeg")
    except:
        print(f"Oops! {sys.exc_info()[0]} occurred.")
    else:
        print('Image loaded successfully!')
        #print(f"{im.format}, {im.size}, {im.mode}")
        print(f'Image size: {im.size[0]} x {im.size[1]}')

if __name__ == '__main__':
    main()
