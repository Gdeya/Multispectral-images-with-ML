import glob
import os
for folder_name in glob.glob('..\\unprocessed_img\\*'):
    for file_path in glob.glob(folder_name + '\\*'):
        str_container = file_path.split('\\')
        new_path = file_path.replace('DJI',str_container[-2])
        os.rename(file_path,new_path)