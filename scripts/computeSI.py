
import PIL
from PIL import Image, ImageFilter, ImageChops
import os
import random
from glob import glob
import os.path as op
import pandas as pd
from os import listdir
from os.path import isfile, join
from os import walk
import numpy as np

base_dir = "/media/noor/DataNS/Imagesets/DNimal_I_background/masks"
obj_dirs = glob(op.join(base_dir, 'object'))
objplus_dirs = glob(op.join(base_dir, 'object+'))

def diff_images(img1, img2, d1):

  diff1 = ImageChops.subtract(img1,img2)
  diff2 = ImageChops.subtract(img2,img1)
  diff1.save(d1)
  #diff2.save(d2)


for obj_dir in obj_dirs:
    images = glob(op.join(obj_dir, '*', '*.png'))
    for image in images:
        imageplus = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/object+/',image.split("/")[-2], image.split("/")[-1])
        img = Image.open(image)
        imgplus = Image.open(imageplus)

        if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/background/',image.split("/")[-2])):
            os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/background/',image.split("/")[-2]))
        dname1 = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/background/',image.split("/")[-2], image.split("/")[-1])

        diff_images(img,imgplus,dname1)
