import os
import pandas as pd

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_1_co2a0000364'


i = 0
os.chdir(dir_name)
for filename in os.listdir(dir_name):
    if filename.endswith(".pkl"):
        data = pd.read_table(filename,names=['col 1','col 2','col 3','col 4'])
        data.to_csv('new_csv_file_'+str(i)+'.csv',index=False)
        i=i+1
'''
gzip panda cre_pick
'''
