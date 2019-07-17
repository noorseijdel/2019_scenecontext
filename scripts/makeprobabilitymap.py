from PIL import Image
import os
import random
from glob import glob
import os.path as op
import pandas as pd
import numpy as np
import pylab as plt
from pylab import text
from scipy import misc
#load file with network classifcation (probability of correct object)
resnets = ['resnet10', 'resnet18', 'resnet34', 'resnet50','resnet101','resnet152']
#resnets = ['resnet34']
catIDs = [403,405,436,449,469,473,488,496,535,580,621,628,633,638,651,652,704,725,743,762,766,780,783,815,818,847,893]

for resnet in resnets:
    print(resnet)
    for catID in catIDs:
        print(catID)
        imgs_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/Normal/'+resnet+'_atypical_prob.txt'
        patched_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/patch128/'+resnet+'_atypical_'+str(catID)+'_patch128_prob.txt'
        #patchsize = [64, 225]
        patchsize = [128, 169]
        #patchsize = [256, 255]


        df_imgs = pd.read_csv(imgs_file, sep=',')
        df_imgs = df_imgs[df_imgs['img'].str.contains('/'+str(catID))]
        df_patches = pd.read_csv(patched_file, sep=',')


        for imIdx, imRow in df_imgs.iterrows():
            imID = imRow['img']
            origProb = imRow['corProb']
            #print(imID.rsplit('/')[-1])
            #print(imID)
            patches = df_patches[df_patches['img'].str.contains(imID)]
            #print(patches)
            patches = patches.reset_index(drop=True)
            probmap = np.full((512, 512, patchsize[1]), np.nan)
            coordinates = []
            for xc in range(0,(544-(patchsize[0])), 32):
                for yc in range(0, (544-(patchsize[0])), 32):
                    coordinates.append((xc,yc))
            #print(len(coordinates))

            for loci in range(patchsize[1]):
                for patchx in range(patchsize[0]):
                    for patchy in range(patchsize[0]):
                        probmap[coordinates[loci][0]+patchx, coordinates[loci][1]+patchy, loci] = origProb-(patches['corProb'][loci])
    #        print(probmap)
                    #np.put(probmap, (coordinates[loci][0] + patchsize, coordinates[loci][1] + patchsize, loci), origProb-(patches['corProb'][loci]))
                    #print(coordinates[loci][0] + patchsize)
            meanarray = np.nanmean(probmap, axis=2)
            meanmap = pd.DataFrame(meanarray)
            #print((os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/',imID.rsplit('/',1)[-2], imID[-32:])))
            if not os.path.exists(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch'+ str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2])):
                os.makedirs(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2]))
            #print(imID[-36:])
            meanmap.to_csv(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/',(imID.rsplit('/')[-3]), imID.rsplit('/')[-2], imID[-20:]+ '_probmap_'+resnet+'.csv'))
            im = plt.imshow(meanmap, cmap='viridis')
            plt.axis('equal')
            text(3, 3,str(origProb))
            plt.colorbar(im, orientation='vertical')
            plt.clim(-0.2,0.8)
            plt.title('ImgID: %s' % imID)
            #plt.savefig(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) +'/',(imID.rsplit('/')[-3]),imID.rsplit('/')[-2],imID[-20:]+'_probmap_'+resnet+'.jpg'))   # save the figure to file
            plt.clf() ; plt.cla()
            #plt.show()
           # print a.shape