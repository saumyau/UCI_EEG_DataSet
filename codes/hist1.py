import os
from scipy.stats.stats import pearsonr
import pickle as pl
from nltk.tokenize import word_tokenize
import pandas as pd
from operator import itemgetter
import pylab as plt
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np
from pandas import plotting
#pandas.plotting.scatter_matrix
dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_m_co2a0000364'

os.chdir(dir_name)
arr = np.array([])

arrays = np.array(['channel','frequency','voltage'])
with open("test_data_1.txt",'r') as q:
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
#df = pd.DataFrame(np.array([['Y','255',float(-18.0345)]]), columns=['channel', 'frequency', 'voltage']).append(df)
#df = pd.DataFrame(np.array([['Y','255',float(-18.0345)]]), columns=['channel', 'frequency', 'voltage']).append(df)

#print(df['voltage'])
#arr = np.split(df['voltage'],64)
arr = df['voltage']
#print(arr)

final = np.array([])
for i in range(64):
    new = np.arange(256)
    final = np.append(final,new)

final1 = [i for i in range(256*64)]
k = np.std(arr)
print(k)
final1 = np.append(final1,[i for i in range(62)])
print(len(arr))
print(len(final))
print(len(final1))


n, bins, patches = plt.hist(arr, 64, normed=1, facecolor='g', alpha=0.75)
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([1, 16446, -2, 10])
plt.grid(True)
plt.hist(arr,bins=64, normed=True,histtype ='step')
#plt.show()
#plt.hist(arr,final1)
plt.bar(final1, arr, align='center')
#plt.show()
#bar(arr,final1)
bar(final1, arr, width=1, align='center', color='brown')
#plot(final1, arr, color='purple', lw=1, marker='.')
plt.ylabel('volt');
#plotting.scatter_matrix(df[['frequency', 'voltage']])

plt.show()


'''
stastical analysis:
1) find mean of alc and conrl with 3 types of stimulus each. so find 6 means.
2) find SD for same
3) perform t-test on each pair of stimulus of alc and contrl
4) maybe perform anova within a group (not so required)
5) z-test,f-test,chisq
6) normal poisson bernoulli distribution

'''
