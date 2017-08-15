import os, tarfile

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_n_co2a0000364\\'
ext='.gz'

os.chdir(dir_name)

for item in os.listdir(dir_name):
    if item.endswith(ext):
        file_name=os.path.abspath(item)
        tar_ref=tarfile.open(file_name)
        tar_ref.extractall(dir_name)
        tar_ref.close()
        os.remove(file_name)
