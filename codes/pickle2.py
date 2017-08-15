import os, pickle

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_m_co2a0000364'


os.chdir(dir_name)

with open("co2a0000364.rd.009.gz.pkl",'rb') as infile:
    newObj = pickle.load(infile)

print(newObj)
