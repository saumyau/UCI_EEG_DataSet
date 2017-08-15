from matplotlib import style
import numpy as np
import os
import pickle as pl
from nltk.tokenize import word_tokenize
import pandas as pd
from Columns import Columns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.plotly as py
import plotly.graph_objs as go

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_m_co2a0000364'

os.chdir(dir_name)

f = open('new_csv_file_1.csv','r')
ff = open('test_data_1.txt','w')
with open("pick_cre_1.pkl",'wb') as outfile:
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

x_start, x_end = 0, 64 
y_start, y_end = 0, 64
x1 = np.array([])
y1 = np.array([])
z1 = np.array([])
z11= np.array([])
double_x1=np.zeros((64, 255))
double_y1=np.zeros((64, 255))
#xw1 = np.array([])
#yw1 = np.array([])

temp=1
fig = plt.figure()
#ax1 = fig.add_subplot(111,projection='3d')

with open("test_data_1.txt",'r') as q:
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    for line in q:
        arrays = np.fromstring(str(line),dtype=float,sep=',')
        #print(arrays)
        if(len(arrays)==0):
            z11 = np.full((1,1),temp)
            temp=temp+1
            continue
        x1 = np.append(x1,[arrays[0]])
        y1 = np.append(y1,[arrays[1]])
        z1 = np.append(z1,[z11])
        
z1 = np.append(z1,np.full((1,255),64))
#print(len(x1)) #2^14-1
#print(len(y1))
#print(len(z1))

'''
minval = y1[0]
maxval = y1[0]
for i in y1:
    if i < minval:
       minval = i
    if i > maxval:
       maxval = i
dx = np.ones(64*255)
dy = np.'''
#print(arrays)
#print(y1)
for i in range(64):
    ax1 = fig.add_subplot(8,8,i+1)
    ax1.plot([x1[j] for j in range(i*255,(i+1)*255)],[y1[j] for j in range(i*255,(i+1)*255)], 'c')
    ax1.set_xlabel('x axis')
    #ax1.set_ylabel('y axis')

plt.show()
#x,y = np.genfromtxt('test_data.txt',usecols=np.arange(0,2))

