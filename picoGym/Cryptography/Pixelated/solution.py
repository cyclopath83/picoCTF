#!/usr/bin/env python

import numpy as np
from PIL import Image



def main():
    img1 = np.array(Image.open("scrambled1.png"))
    img2 = np.array(Image.open("scrambled2.png"))

    img = img1 + img2
    Image.fromarray(img).save('scrambled.png')

    

if __name__ == '__main__':
    main()

