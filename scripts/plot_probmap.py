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

map2plot = '/media/noor/DataNS/Onderzoek/Projects/Backgroundtypicality/Maps/patch128/a_background/403/val_00002062image034_probmap_resnet10'

meanmap = pd.read_csv(map2plot+'.csv')
meanmap = resize(meanmap,(512,512))

#meanmap = np.array(Image.fromarray(meanmap).resize(512, 512))

im = plt.imshow(meanmap, cmap='viridis')
plt.axis('equal')
#text(3, 3,str(origProb))
plt.colorbar(im, orientation='vertical')
plt.clim(-0.2,0.8)
plt.title('ImgID: %s' % map2plot[:-10])
plt.savefig(os.path.join(map2plot+'.jpg'))   # save the figure to file
plt.clf() ; plt.cla()