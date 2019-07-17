from PIL import Image
import os
import random
from glob import glob
import os.path as op
import pandas as pd
import numpy as np
import pylab as plt
from pylab import text
from skimage.transform import resize

base_dir = '/media/noor/DataNS/Imagesets/DNimal_I_background/all_good'
obj_dirs = glob(op.join(base_dir, '*'))
print(obj_dirs)

for obj_dir in obj_dirs:
    sub_dirs = glob(op.join(obj_dir, '*.png'))
    for image in sub_dirs:
        im = Image.open(image)
        pixel_data = im.load()
        if im.mode == "RGBA":
            for y in xrange(im.size[1]): # For each row ...
                for x in xrange(im.size[0]): # Iterate through each column ...
                # Check if it's opaque
                    if pixel_data[x, y][3] < 255:
                # Replace the pixel data with the colour white
                        pixel_data[x, y] = (255, 255, 255, 255)
                    else:
                        pixel_data[x, y] = (0, 0, 0, 0)
        im = im.convert('RGB')
        # Resize the image thumbnail
        im.thumbnail([512, 512], Image.ANTIALIAS)
        if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masking/', image.split("/")[-2])):
            os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masking/', image.split("/")[-2]))
        newfilename = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masking/', image.split("/")[-2], image.split("/")[-1])
        print(newfilename)
        #newfilename = newfilename.replace(".png_", "")
        im.save(newfilename)
