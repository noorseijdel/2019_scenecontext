
import PIL
from PIL import Image, ImageFilter, ImageDraw
import os
from glob import glob
import os.path as op
from os import listdir
from os.path import isfile, join
import numpy as np
import scipy.misc

base_dir = "/media/noor/DataNS/Imagesets/DNimal_I_background/real_wb"
obj_dirs = glob(op.join(base_dir, '*', 'Segmented'))

for obj_dir in obj_dirs:
    images = glob(op.join(obj_dir, '*.png'))
    #print images
    for image in images:
        im = Image.open(image)
        img = im.convert("RGBA")
        pixdata = img.load()
        width, height = img.size

        imag = Image.new('RGBA', (height, width), color =255)
        draw1 = ImageDraw.Draw(imag)
        imageplus = Image.new('RGBA', (height, width), color=(1,1,1,255))
        draw2 = ImageDraw.Draw(imageplus)

        for y in xrange(height):
            for x in xrange(width):
#                print pixdata[x,y]
                if pixdata[x,y][3] != 0:
                    if x>1 and y>1 or x<511 and y<511:
                        draw1.ellipse((x-1,y-1,x+1,y+1),fill = (1,1,1,255))
                    if x>25 and y>25 or x<487 and y<487:
                        draw2.ellipse((x-25,y-25,x+25,y+25), fill = (0,0,0,0))
                else:
                    pixdata[x, y] = (1, 1, 1, 255)

        """
        if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/object/', obj_dir.split("/")[-2])):
            os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/object/', obj_dir.split("/")[-2]))
        newfilename = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/object/', obj_dir.split("/")[-2], image.split("/")[-1])
        #print newfilename
        imag.save(newfilename, "PNG")


        if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/object+/', obj_dir.split("/")[-2])):
            os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/object+/', obj_dir.split("/")[-2]))
        newfileplus = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/object+/', obj_dir.split("/")[-2], image.split("/")[-1])
        #print newfileplus
        imageplus.save(newfileplus, "PNG")
        """

        if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/background/', obj_dir.split("/")[-2])):
            os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/background/', obj_dir.split("/")[-2]))
        bg = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masks/background/', obj_dir.split("/")[-2], image.split("/")[-1])

        Image.alpha_composite(imag,imageplus).save(bg)
