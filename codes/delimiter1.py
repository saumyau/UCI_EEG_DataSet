import os, tarfile, gzip, linecache

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_m_co2a0000364'

os.chdir(dir_name)

with open('new_csv_file.csv') as infile, open('outfile.csv', 'w') as outfile:
    #line = linecache.getline('new_csv_file.csv', 6)
    outfile.write(','.join(infile.read().split('\s')) + '\n')
