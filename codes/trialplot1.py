import os
from matplotlib import style
import numpy as np

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_1_co2a0000364'

os.chdir(dir_name)

style.use('ggplot')

x,y = np.loadtxt('new_csv_file.csv',unpack=True,delimiter=' ')

plt.plot(x,y)
plt.show()
