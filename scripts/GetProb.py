import pandas as pd
import numpy as np
import re
import glob
import os

#Read list of files with white background
#datalist = glob.glob('/media/noor/DataNS/Imagesets/DNimal_I_background/model_performance_stim_patched/models/patch256/resnet*[0-152]*_a_*.txt')
datalist = glob.glob('/media/noor/DataNS/Imagesets/DNimal_I_background/model_performance_stim_patched/models/patch128/resnet34_a_*.txt')
print(datalist)

for dat in datalist:
    #print(dat)

    filename = dat.rsplit('/',1)[-1]
    filename = filename.replace('_a_','_atypical_')
    filename = filename.replace('.txt', '')
    filename = filename + '_prob.txt'

    print(filename)


    data = pd.read_table(dat, delimiter='\t', names=('ind', 'prob', 'cat'))

    #print(data['ind'][0])

    data['corAns'] = data['ind'].str.extract('%s(.*)%s' % ('a_background/', '/ILS'), expand=False)
    data['img'] = data['ind'].str.extract('%s(.*)%s' % ('/stim_patched128/', '' ), expand=False)
    data['corProb'] = 0.0
    data['Top'] = 0

    data.ind = pd.to_numeric(data['ind'], errors='coerce').fillna(0)
    data.corAns = pd.to_numeric(data['corAns'], errors='coerce').fillna(0)

    correct_count = 0
    for i in range(0,(len(data)),6):
        for ii in range(1,6):
            if data['corAns'][i]==data['ind'][i+ii]:
                data['corProb'][i]=data['prob'][i+ii]
                data['Top'][i]=ii
                correct_count = correct_count + 1

    instances =(len(data)/6)

    #print(["accuracy: " , float(correct_count)/float(instances)])

    data2save = data.dropna(subset=['img'])
    data2save.to_csv(os.path.join('/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/patch128',filename),columns=['img', 'corProb', 'Top'])

