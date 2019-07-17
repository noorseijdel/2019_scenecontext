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



resnets = ['resnet18']
catIDs = [815,818,847,893]
conditions = ['white']

patchsize = [256, 81]
for condition in conditions:
    for resnet in resnets:
        print(resnet)
        for catID in catIDs:
            print(catID)
            imgs_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/Normal/'+resnet+'_'+ condition +'_nosoftmax_logits.txt'
            patched_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/patch256/'+resnet+'_'+ condition[0] + '_'+str(catID)+'_patch256_nosoftmax_logits.txt'

            df_imgs = pd.read_csv(imgs_file, sep=',')
            df_imgs = df_imgs[df_imgs['img'].str.contains('/'+str(catID))]
            df_patches = pd.read_csv(patched_file, sep=',')

            for imIdx, imRow in df_imgs.iterrows():
                imID = imRow['img']
                imID = imID.replace('.png','')
                origProb = imRow['corProb']

                patches = df_patches[df_patches['img'].str.contains(imID)]

                patchsize[1] = len(patches)

                patches = patches.reset_index(drop=True)
                probmap = np.full((512, 512, patchsize[1]), np.nan)
                coordinates = []
                for xc in range(0,(544-(patchsize[0])), 32):
                    for yc in range(0, (544-(patchsize[0])), 32):
                        coordinates.append((xc,yc))

                for loci in range(patchsize[1]):
                    for patchx in range(patchsize[0]):
                        for patchy in range(patchsize[0]):
                            probmap[coordinates[loci][0]+patchx, coordinates[loci][1]+patchy, loci] = origProb-(patches['corProb'][loci])

                meanarray = np.nanmean(probmap, axis=2)
                meanmap = pd.DataFrame(meanarray)

                if not os.path.exists(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch'+ str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2])):
                    os.makedirs(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2]))

                meanmap.to_csv(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/',(imID.rsplit('/')[-3]), imID.rsplit('/')[-2], imID[-20:]+ '_probmap_'+resnet+'.csv'))


resnets = ['resnet34', 'resnet50','resnet101','resnet152']
catIDs = [403,405,436,449,469,473,488,496,535,580,621,628,633,638,651,652,704,725,743,762,766,780,783,815,818,847,893]
conditions = ['white']

patchsize = [256, 81]
for condition in conditions:
    for resnet in resnets:
        print(resnet)
        for catID in catIDs:
            print(catID)
            imgs_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/Normal/'+resnet+'_'+ condition +'_nosoftmax_logits.txt'
            patched_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/patch256/'+resnet+'_'+ condition[0] + '_'+str(catID)+'_patch256_nosoftmax_logits.txt'

            df_imgs = pd.read_csv(imgs_file, sep=',')
            df_imgs = df_imgs[df_imgs['img'].str.contains('/'+str(catID))]
            df_patches = pd.read_csv(patched_file, sep=',')

            for imIdx, imRow in df_imgs.iterrows():
                imID = imRow['img']
                imID = imID.replace('.png','')
                origProb = imRow['corProb']

                patches = df_patches[df_patches['img'].str.contains(imID)]

                patchsize[1] = len(patches)

                patches = patches.reset_index(drop=True)
                probmap = np.full((512, 512, patchsize[1]), np.nan)
                coordinates = []
                for xc in range(0,(544-(patchsize[0])), 32):
                    for yc in range(0, (544-(patchsize[0])), 32):
                        coordinates.append((xc,yc))

                for loci in range(patchsize[1]):
                    for patchx in range(patchsize[0]):
                        for patchy in range(patchsize[0]):
                            probmap[coordinates[loci][0]+patchx, coordinates[loci][1]+patchy, loci] = origProb-(patches['corProb'][loci])

                meanarray = np.nanmean(probmap, axis=2)
                meanmap = pd.DataFrame(meanarray)

                if not os.path.exists(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch'+ str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2])):
                    os.makedirs(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2]))

                meanmap.to_csv(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/',(imID.rsplit('/')[-3]), imID.rsplit('/')[-2], imID[-20:]+ '_probmap_'+resnet+'.csv'))

resnets = ['resnet10', 'resnet18','resnet34', 'resnet50','resnet101','resnet152']
catIDs = [403,405,436,449,469,473,488,496,535,580,621,628,633,638,651,652,704,725,743,762,766,780,783,815,818,847,893]
conditions = ['typical', 'atypical']

patchsize = [256, 81]
for condition in conditions:
    for resnet in resnets:
        print(resnet)
        for catID in catIDs:
            print(catID)
            imgs_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/Normal/'+resnet+'_'+ condition +'_nosoftmax_logits.txt'
            patched_file = '/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/patch256/'+resnet+'_'+ condition[0] + '_'+str(catID)+'_patch256_nosoftmax_logits.txt'

            df_imgs = pd.read_csv(imgs_file, sep=',')
            df_imgs = df_imgs[df_imgs['img'].str.contains('/'+str(catID))]
            df_patches = pd.read_csv(patched_file, sep=',')

            for imIdx, imRow in df_imgs.iterrows():
                imID = imRow['img']
                imID = imID.replace('.png','')
                origProb = imRow['corProb']

                patches = df_patches[df_patches['img'].str.contains(imID)]

                patchsize[1] = len(patches)

                patches = patches.reset_index(drop=True)
                probmap = np.full((512, 512, patchsize[1]), np.nan)
                coordinates = []
                for xc in range(0,(544-(patchsize[0])), 32):
                    for yc in range(0, (544-(patchsize[0])), 32):
                        coordinates.append((xc,yc))

                for loci in range(patchsize[1]):
                    for patchx in range(patchsize[0]):
                        for patchy in range(patchsize[0]):
                            probmap[coordinates[loci][0]+patchx, coordinates[loci][1]+patchy, loci] = origProb-(patches['corProb'][loci])

                meanarray = np.nanmean(probmap, axis=2)
                meanmap = pd.DataFrame(meanarray)

                if not os.path.exists(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch'+ str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2])):
                    os.makedirs(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/', imID.rsplit('/')[-3], imID.rsplit('/')[-2]))

                meanmap.to_csv(os.path.join('/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch' + str(patchsize[0]) + '/',(imID.rsplit('/')[-3]), imID.rsplit('/')[-2], imID[-20:]+ '_probmap_'+resnet+'.csv'))
