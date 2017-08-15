from matplotlib import style
import numpy as np
import os
import pickle as pl
from nltk.tokenize import word_tokenize
import pandas as pd
from Columns import Columns
import matplotlib.pyplot as plt


dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_m_co2a0000364'

os.chdir(dir_name)

f = open('new_csv_file_0.csv','r')
ff = open('test_data_0.txt','w')
with open("pick_cre_0.pkl",'wb') as outfile:
    for l in f:
    #print(l)
        cols = word_tokenize(l)
    #print(cols)
        myObj = Columns(cols[2],cols[3])
        #print(str(myObj))
        #str = ' '.join(myObj)
        ff.write(str(myObj))


ff.close()
style.use('ggplot')

x_start, x_end = 0, 255 
y_start, y_end = 0, 255
x1 = np.array([])
y1 = np.array([])
            
with open("test_data_0.txt",'r') as q:
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    for line in q:
        arrays = np.fromstring(str(line),dtype=float,sep=',')
        if(len(arrays)==0):
            x = x1[x_start:x_end]
            y = y1[y_start:y_end]
            plt.plot(x,y)
            plt.show()
            x1 = np.array([])
            y1 = np.array([])
            continue
        x1 = np.append(x1,[arrays[0]])
        y1 = np.append(y1,[arrays[1]])
#x,y = np.genfromtxt('test_data.txt',usecols=np.arange(0,2))

