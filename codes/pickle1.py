import os, pickle

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_1_co2a0000364'
os.chdir(dir_name)

dict1 = {'a':100,'b':200,'c':300}
list1 = [400,500,600]

print(dict1)
print(list1)

output = open("save1.pkl",'wb')

pickle.dump(dict1,output)
pickle.dump(list1,output)
output.close()

