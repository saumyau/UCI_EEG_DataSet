import os
import pickle as pl
from nltk.tokenize import word_tokenize
from Columns_seaborn import Columns_seaborn


dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\c_n_co2c0000337'

os.chdir(dir_name)

i = 0
for filename in os.listdir(dir_name):
    if filename.endswith(".csv"):
        f = open('new_csv_file_'+str(i)+'.csv','r')
        ff = open('test_data_'+str(i)+'.txt','w')
        with open('pick_cre_'+str(i)+'.pkl','wb') as outfile:
            for l in f:
                cols = word_tokenize(l)
                myObj = Columns_seaborn(cols[1],cols[2],cols[3])
                ff.write(str(myObj))
                pl.dump(myObj,outfile)
        i=i+1

ff.close()


