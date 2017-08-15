import pickle, os
from nltk.tokenize import word_tokenize
from Columns import Columns

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_1_co2a0000364'

os.chdir(dir_name)

f = open('new_csv_file.csv','r')

with open("pick_cre.pkl",'wb') as outfile:
    for l in f:
    #print(l)
        cols = word_tokenize(l)
    #print(cols)
    #myObj = Columns(cols[0],cols[1],cols[2],cols[3])
        pickle.dump(cols,outfile)  

