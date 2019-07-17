from PIL import Image
import os
import random
from glob import glob
import os.path as op
import pandas as pd


base_dir = "/media/noor/DataNS/Imagesets/DNimal_I_background/all_good"
obj_dirs = glob(op.join(base_dir, '*'))

#load file with background categories
bg_file = '/media/noor/DataNS/Onderzoek/Projects/ManvsMachine/backgrounds_list_2018.csv'

df = pd.read_csv(bg_file, sep=',')
df = df.set_index('object')

for obj_dir in obj_dirs:
    sub_dirs = glob(op.join(obj_dir,'*.png'))
    for image in sub_dirs:
        im = Image.open(image)
        im = im.resize((170,170), Image.ANTIALIAS)
        ob = Image.new('RGBA',(512,512),(0,0,0,0))
        ob.paste(im,(0,0), mask=im)
        #ob.show()
        objectidx = 'o'+image.split("/")[-2]

        df2 = df.loc[objectidx]
        lst_atypical = df.loc[objectidx]['atypical'].split(',')
        lst_atypical = [s.replace("'", "") for s in lst_atypical]
        lst_atypical = [k.replace(" ", "") for k in lst_atypical]
        lst_atypical = [a[1:] for a in lst_atypical]
        bg_atyp = random.choice(lst_atypical)

        usepath = os.path.join('/media/noor/DataNS/Imagesets/SUN/SUN2012/SUN2012', bg_atyp)
        for bg_im in os.listdir(os.path.join('/media/noor/DataNS/Imagesets/SUN/SUN2012/SUN2012', bg_atyp)):
            background = Image.open(os.path.join('/media/noor/DataNS/Imagesets/SUN/SUN2012/SUN2012', bg_atyp, bg_im))
            background2 = background.convert("RGBA")

            result = Image.alpha_composite(background2, ob)
            #print(image.split("/")[-1])

            if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 'a_background', 'loc1')):
                os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 'a_background', 'loc1'))

            newfilename = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 'a_background', 'loc1',bg_im)
            #print(bg_im)
                #newfilename = newfilename.replace(".png/", "/")
            result.save(newfilename)

        ## NOW THE SAME FOR A TYPICAL BACKGROUND
        lst_typical = df.loc[objectidx]['typical'].split(',')
        lst_typical = [s.replace("'", "") for s in lst_typical]
        lst_typical = [k.replace(" ", "") for k in lst_typical]
        lst_typical = [a[1:] for a in lst_typical]
        bg_typ = random.choice(lst_typical)

        usepath = os.path.join('/media/noor/DataNS/Imagesets/SUN/SUN2012/SUN2012', bg_typ)
        for bg_im in os.listdir(os.path.join('/media/noor/DataNS/Imagesets/SUN/SUN2012/SUN2012', bg_typ)):
            background = Image.open(os.path.join('/media/noor/DataNS/Imagesets/SUN/SUN2012/SUN2012', bg_typ, bg_im))
            background2 = background.convert("RGBA")

            result = Image.alpha_composite(background2, ob)

            if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 't_background', 'loc1')):
                os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 't_background', 'loc1'))

            newfilename = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 't_background', 'loc1',bg_im)
                #newfilename = newfilename.replace(".png/", "/")
            result.save(newfilename)


        #AND FOR WHITE background
        background = Image.open('/media/noor/DataNS/Imagesets/blank.jpg')
        background2 = background.convert("RGBA")
        result = Image.alpha_composite(background2, ob)

        if not os.path.exists(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 'w_background', 'loc1')):
            os.makedirs(os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 'w_background', 'loc1'))

        newfilename = os.path.join('/media/noor/DataNS/Imagesets/DNimal_I_background/humanstim/', image.split("/")[-2], image.split("/")[-1], 'w_background', 'loc1',bg_im)
            #newfilename = newfilename.replace(".png/", "/")
        result.save(newfilename)
