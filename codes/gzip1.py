import os, tarfile, gzip, glob

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_m_co2a0000364'
ext='.gz'

os.chdir(dir_name)

for item in os.listdir(dir_name):
    if item.endswith(ext):
        file_name=os.path.abspath(item)
        with gzip.open(file_name,'rb') as infile:
            with open(file_name+".pkl",'wb') as outfile:
                for line in infile:
                    outfile.write(line)
        #os.remove(file_name)
