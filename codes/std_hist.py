import os
from scipy.stats.stats import pearsonr
import pickle as pl
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
from pandas import plotting

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data'

i = 0
os.chdir(dir_name)
stdarr = np.array([])
new_arr = np.array([])
      
with open('std_file.txt','w') as g:
    for folder in os.listdir(dir_name):
        if(folder!="std_file.txt" and folder!="mean_file.txt"):
            os.chdir(dir_name+"\\"+folder)
            meanarr = np.array([])
            for filename in os.listdir(dir_name+"\\"+folder):
                if filename.endswith(".txt"):
                    #print(os.getcwd())
                    with open(filename,'r') as q:
                        new_arr = np.array([])
                        q.readline()
                        q.readline()
                        q.readline()
                        q.readline()
                        q.readline()
                        q.readline()
                        q.readline()
                        for line in q:
                            arrays1 = np.array(str(line).split(','))
                            k = np.array([arrays1[2]])
                            #print(type(arrays1))
                            new_arr = np.append(new_arr,k.astype(np.float))
                        stdarry = np.std(new_arr)
                        stdarr = np.append(stdarr,stdarry)
                        #print(meanarr)
                        i=i+1
            #os.chdir(dir_name+"\\"+folder)
        #os.chdir(dir_name)
                        if(len(stdarr)==10):
                            g.write(str(stdarr)+"\n")

g.close()

'''
with open('test_data_1.txt','r') as q:
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    for line in q:
        arrays1 = np.array(str(line).split(','))
        k = np.array([arrays1[2]])
        #print(type(arrays1))
        new_arr = np.append(new_arr,k.astype(np.float))
    print(np.mean(new_arr))
    
'''
