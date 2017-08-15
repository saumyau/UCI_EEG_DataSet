from matplotlib import style
import numpy as np
import os
import pickle as pl
from nltk.tokenize import word_tokenize
import pandas as pd
from Columns_seaborn import Columns_seaborn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\c_1_co2c0000337'

os.chdir(dir_name)

arrx1 = np.array([])
arrays = np.array(['channel','frequency','voltage'])
with open("test_data_7.txt",'r') as q:
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    q.readline()
    for line in q:
        arrays1 = np.array(str(line).split(','))
        #arrx = [arrays1[1]]
        #arry = [arrays1[2]]
        arr = np.array(arrays1[0:3])
        #x1 = np.append(x1,arrx)
        #y1 = np.append(y1,arry)
        arrays = np.vstack([arrays,arr])

#arrays_x = list(map(float, x1))
#arrays_y = list(map(float, y1))
#arrays_xy = np.vstack([arrays_x,arrays_y])
#print(arrays)
df = pd.DataFrame(data=arrays[1:,1:],index=arrays[1:,0],columns=arrays[0,1:])
cols = df[['frequency','voltage']]
#print(df.number.values)
df.voltage = df.voltage.astype(float).fillna(0.0)
#print(df.voltage.values)

sum = 0.0
k=1
for i in df['voltage']:
    if(k%255==0):
        avg=sum/255.0
        arr_temp = np.array([avg])
        arrx1 = np.append(arrx1,arr_temp)
        sum = 0.0
        k=k+1
        continue
    sum=sum+i
    k=k+1
    
#print(len(arrx1))

numbs = np.arange(1,65)

new_arr = np.column_stack((numbs,arrx1))

sns.set()
ax = sns.heatmap(new_arr)
#ax = sns.heatmap(new_arr, vmin=0, vmax=1)
plt.show()
