import os
from scipy.stats.stats import pearsonr
import numpy as np
import pickle as pl
from nltk.tokenize import word_tokenize
import pandas as pd
from operator import itemgetter


dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\c_1_co2c0000337'

os.chdir(dir_name)
arr = np.array([])

arrays = np.array(['channel','frequency','voltage'])
with open("test_data_6.txt",'r') as q:
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

df = pd.DataFrame(data=arrays[1:,1:],index=arrays[1:,0],columns=arrays[0,1:])
cols = df[['frequency','voltage']]
#print(df.number.values)
df.voltage = df.voltage.astype(float).fillna(0.0)
#print(df.voltage.values)

k=0
#df2 = pd.DataFrame([['Y','255',-18.0345]], columns=['channel', 'frequency', 'voltage'])
#pd.concat(df2,df)
df = pd.DataFrame(np.array([['Y','255',float(-18.0345)]]), columns=['channel', 'frequency', 'voltage']).append(df)
df = pd.DataFrame(np.array([['Y','255',float(-18.0345)]]), columns=['channel', 'frequency', 'voltage']).append(df)


#print(df['voltage'])
arr = np.split(df['voltage'],64)
#print(len(df['voltage'])
#print(arr)
maxx = -2
'''
p = np.array([])
for i in range(1,63):
    for j in range(1,63):
        if(i!=j):
            temp = list([[pearsonr(arr[i],arr[j])]])
            p=np.append(p,temp)
            
    #print(i)
kx = 0
for i in p:
    if(i>=-1 and i<=1):
        if(i>=maxx):
            maxx = i
'''
state=()
xval = 0
yval = 0
st = (-5,10)
for i in range(1,64):
    for j in range(1,64):
        if(i!=j):
            temp = pearsonr(arr[i],arr[j])
            if(temp>st):
                lst = list(temp)
                lst[1]=10
                st = tuple(lst)
                xval = i
                yval = j
            state=state+temp
            

print(xval)
print(yval)           
print(st)

'''
pandas,heatmap,pearson
check 3d graphs, pickle file creation
'''
'''
highest correlation recordings - a_l_co2a0000364
29,30
31,62
31,62
57,58
57,59
29,58
57,58
57,59
57,59
29,58
highest correlation recorings - a_m_co2a0000364
44,47-recording 1
31,62-recording 2
38,62-recording 3
29,58-recording 4
31,62-recording 5
31,62-recording 6
4,6-recording 7
29,58-recording 8
4,6-recording 9
59,60-recording 10
highest correlation recorings - a_n_co2a0000364
31,62
31,62
57,58
44,47
57,58
31,62
29,58
31,62
29,58
31,62
highest correlation recordings - c_1_co2c0000337
22,28
20,48
23,27
1,5
1,5
1,5
1,5
21,23
29,30
23,51
highest correlation recorings - c_m_co2c0000337
1,31
1,5
1,5
50,60
1,33
43,47
1,33
4,5
22,28
1,5
highest correlation recoring - c_n_co2c0000337
1,33 recording 1
1,5 recording 2
22,28 recording 3
22,28 recording 4
1,33 recording 5
29,58 recording 6
1,5 recording 7
29,58 recording 8
1,5 recording 9
29,58 recording 10
'''
