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
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import seaborn as sns
from scipy import stats
#from mayavi import mlab

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_1_co2a0000364'

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

x_start, x_end = 0, 64 
y_start, y_end = 0, 64
x1 = np.array([])
y1 = np.array([])
z1 = np.array([])
z11= np.array([])
temp=1
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

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

z = np.sin(-x1*y1)



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

ax1.plot_wireframe(x1,y1,z1)
#ax1.scatter(x1, y1, z1, c='r', marker='o')
#py.iplot(fig, filename='scatter-mode')
ax1.set_xlabel("X axis")
ax1.set_ylabel("Y axis")
ax1.set_zlabel("Z axis")
#ax1.scatter(x1,y1,z1,c='g',marker='o')

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x1,y1,z1, cmap=plt.cm.coolwarm,rstride=1, cstride=1)

plt.show()

X, Y = np.meshgrid(x1[0:255],y1[0:255],sparse=True)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
    linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()

f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(x1, y1, cmap=cmap, n_levels=60, shade=True);

plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot a sin curve using the x and y axes.
ax.plot(x1, y1, zs=0, zdir='z', label='curve in (x,y)')

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')
x = np.random.sample(20*len(colors))
y = np.random.sample(20*len(colors))
c_list = []
for c in colors:
    c_list.append([c]*20)
# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x,y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x,z)')

# Make legend, set axes limits and labels
ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35)

plt.show()


'''
figure = mlab.figure('DensityPlot')
pts = mlab.points3d(x1, y1, z1, density, scale_mode='none', scale_factor=0.07)
mlab.axes()
mlab.show()
'''
#x,y = np.genfromtxt('test_data.txt',usecols=np.arange(0,2))

