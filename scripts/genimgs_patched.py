from PIL import Image
import os
import random
from glob import glob
import os.path as op
import pandas as pd
import numpy as np

base_dir = '/media/noor/DataNS/Imagesets/DNimal_I_background/stim/a_background'
obj_dirs = glob(op.join(base_dir, '*'))

patch = Image.open('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Analysis/greypatch256.png')
stepsize = 32


for obj_dir in obj_dirs:
    print obj_dir
    sub_dirs = glob(op.join(obj_dir,'*.png'))
    for image in sub_dirs:
        im = Image.open(image)
        #print(im)
        iters = 1
        for yc in range(0,im.size[0]-224, stepsize):
            for xc in range(0, im.size[1]-224, stepsize):
                #print(im.size[1]-96)
                #print(iters)
                image_copy = im.copy()
                image_copy.paste(patch, (xc, yc))

                if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/stim_patched256/a_background/', image.split("/")[-2])):
                    os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/stim_patched256/a_background/', image.split("/")[-2]))

                newfilename = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/stim_patched256/a_background/', image.split("/")[-2], image.split("/")[-1]) + "_" + str(iters).zfill(3)
                newfilename = newfilename.replace(".png", "")
                #print(newfilename)
                image_copy = image_copy.convert("RGB")
                image_copy.save(newfilename, 'jpeg')
                iters = iters+1

