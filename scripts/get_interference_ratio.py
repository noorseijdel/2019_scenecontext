from PIL import Image
import os
from glob import glob
import os.path as op
import pandas as pd
import numpy as np
import csv

resnets = ['resnet10','resnet18','resnet34','resnet50','resnet101', 'resnet152']
#resnets = ['resnet10','resnet152']
conditions =['a_background', 't_background','w_background']
#conditions =['t_background', 'a_background']

all_avgs = np.zeros((3,6,2))

for condi, condition in enumerate(conditions):

    for resi, resnet in enumerate(resnets):
        print(condi, resi)
        indx = 0
        mean_obj_interference = []
        mean_bg_interference = []
        with open('objectinterference_'+ resnet+ '_' + condition, 'wb') as myfile:
            wr = csv.writer(myfile)
            aii = ['condition', 'resnet', 'obj','img', 'obj_interf', 'bg_interf']
            wr.writerow(aii)
            base_dir = '/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch128/' + condition
            obj_dirs = glob(op.join(base_dir, '*'))

            for obj_dir in obj_dirs:
                probmaps = glob(op.join(obj_dir, '*'+ resnet+ '.csv'))
                path2use = op.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masking/object', obj_dir.split("/")[-1])
                path2bg = op.join('/media/noor/DataNS/Imagesets/DNimal_I_background/masking/background', obj_dir.split("/")[-1])
                print(path2use)
                for probmap in probmaps:
                    print(probmap)
                    stri = (probmap.split("/")[-1])[0:12]
                    meanmap = pd.read_csv(probmap)
                    meanmap = meanmap.drop(meanmap.columns[[0]], axis=1)
                    meanmap = np.array(meanmap)
#                    print(meanmap)
                    #print(meanmap.max())

                    object_mask = [i for i in os.listdir(path2use) if os.path.isfile(os.path.join(path2use,i)) and \
                    stri in i]
                    temp = Image.open(op.join(path2use , object_mask[0]))

                    background_mask = [i for i in os.listdir(path2bg) if os.path.isfile(os.path.join(path2bg,i)) and \
                    stri in i]
                    temp_bg = Image.open(op.join(path2bg , background_mask[0]))

                    object_im = temp.convert('1')      # Convert to black&white
                    object_im = np.array(object_im)

                    background_im = temp_bg.convert('1')
                    background_im = np.array(background_im)

                    obj_interference = (meanmap[object_im].mean())
                    bg_interference = (meanmap[background_im].mean())

                    #print(indx)
                    mean_obj_interference.append(obj_interference)
                    mean_bg_interference.append(bg_interference)

                    indx +=1
                    print(obj_interference, bg_interference)
                    aa = [condition, resnet, obj_dir.split("/")[-1],(probmap.split("/")[-1])[0:12], obj_interference, bg_interference]
                    wr.writerow(aa)

        #print(float(sum(mean_obj_interference)) / float(len(mean_obj_interference)))

        #print(float(sum(mean_bg_interference)) / float(len(mean_bg_interference)))


        all_avgs[condi,resi,0] = (sum(mean_obj_interference)) / float(len(mean_obj_interference))
        all_avgs[condi,resi,1] = (sum(mean_bg_interference)) / float(len(mean_bg_interference))

print(all_avgs)