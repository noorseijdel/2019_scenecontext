import pandas as pd
import numpy as np
import re
import glob
import os

#Read list of files with white background
#datalist = glob.glob('/media/noor/DataNS/Imagesets/DNimal_I_background/model_performance_stim_patched/models/patch256/resnet*[0-152]*_a_*.txt')

resnets = ['resnet10','resnet18', 'resnet34', 'resnet50','resnet101', 'resnet152']
conditions =['_a_', '_t_','_w_'] #forpatched

for resnet in resnets:
    for condition in conditions:
        datalist = glob.glob('/media/noor/DataNS/Imagesets/DNimal_I_background/model_performance_stim_patched/logits/patch64/' + resnet + condition + '*softmax.txt')
        print(datalist)

        for dat in datalist:
            #print(dat)

            filename = dat.rsplit('/',1)[-1]
            #filename = filename.replace('_a_','_atypical_')
            filename = filename.replace('.txt', '')
            filename = filename + '_logits.txt'

            print(filename)
            data = pd.read_table(dat, delimiter='\t', names=('ind', 'logits', 'cat'))

            data['corAns'] = data['ind'].str.extract('%s(.*)%s' % ('_background/', '/ILS'), expand=False)
            data['img'] = data['ind'].str.extract('%s(.*)%s' % ('/stim_patched64/', '' ), expand=False)
            data['corProb'] = 0.0

            data.ind = pd.to_numeric(data['ind'], errors='coerce').fillna(0)
            data.corAns = pd.to_numeric(data['corAns'], errors='coerce').fillna(0)

            for i in range(0,(len(data)),2):
                #print(i)
                #print(data['corAns'][i])
                #print(data['ind'][i+1])
                data['corProb'][i]=data['logits'][i+1]

            data2save = data.dropna(subset=['img'])
            data2save.to_csv(os.path.join('/media/noor/DataNS/Onderzoek/Projects/ResNetDepth_analysisfiles/Probability/patch64',filename),columns=['img', 'corProb'])

