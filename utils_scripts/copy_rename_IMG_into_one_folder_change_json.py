# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:20:05 2020
script to copy all img from one project into one folder and give every img the name of the subfolder (example BK5)
@author: sven
"""
import os
import ntpath
import shutil
import numpy as np
import json
#%% change rotedir and path_dst_folder
##check if folder dataset_9091 mit IMG in Subordner 
rootdir = 'E:\Datasets_GGU_Bodenproben_orig\Bodenproben_recognition\dataset\dataset_8205_1\8205_1'

# set True to change and False do nothing
copy_img_into_one_folder = True #True#False

path_dst_folder = 'E:\\Datasets_GGU_Bodenproben_orig\\Bodenproben_recognition\\dataset\\dataset_8205_1\\all_img'

change_json = False #True #False

if change_json == True: 
    #load json file
    #f = open('E:\\Datasets_GGU_Bodenproben_orig\\Bodenproben_recognition\\dataset\\dataset_9091\\all_img\\train_0247_5205\\recognice_sample_train_5205.json',)
    f = open('E:\\Datasets_GGU_Bodenproben_orig\\Bodenproben_recognition\\dataset\\dataset_9091\\all_img\\val_5206_5272\\recognice_sample_val_5206_5272.json',)
    
    #json_train or json_val in new folder allimg
    #path_json_edit = 'E:\\Datasets_GGU_Bodenproben_orig\\Bodenproben_recognition\\dataset\\dataset_9091\\all_img2\\train_0247_5205\\recognice_sample_train_5205_edit.json'
    path_json_edit = 'E:\\Datasets_GGU_Bodenproben_orig\\Bodenproben_recognition\\dataset\\dataset_9091\\all_img2\\val_5206_5272\\recognice_sample_val_5206_5272_edit.json'
    
    data = json.load(f)
#%%
number_img = 0
number_matches_json_allimg = 0
no_match = 0
fileall = []
data_filename = []
split_path_file_img_and_extension_sum = []
basename_img_file_all = []
file_all2 = []
files_all = []
dirs_all = []
matchings = []

#check if JPG and get folder name for copied img 
for subdir, dirs, files in os.walk(rootdir):
#    files_all.append(files)
#    dirs_all.append(dirs)
    for file in files:
        number_img = number_img + 1
        path_file_img = os.path.join(subdir,file)
        split_path_file_img_and_extension = os.path.splitext(path_file_img)
        #        file_all2.append(file)
        if (split_path_file_img_and_extension[1] == '.jpg' or split_path_file_img_and_extension[1] == '.JPG') :
#            split_path_file_img_and_extension_sum.append(split_path_file_img_and_extension[1])
            get_name_from_copied_folder = ntpath.basename(subdir)
            filename_with_foldername_path = split_path_file_img_and_extension[0]+ get_name_from_copied_folder+ split_path_file_img_and_extension[1]
       
# copy img and include foldername into filename  
            src = path_file_img
            basename = os.path.basename(filename_with_foldername_path)
            dst = os.path.join(path_dst_folder,basename)
            if copy_img_into_one_folder == True:
                shutil.copyfile(src,dst) 
                
            if change_json == True:     
                basename_img_file =  os.path.basename(split_path_file_img_and_extension[0])
    # change img names in json file
                data_keys_json = list(data.keys())#['IMG_0332.JPG1076716']
    #            basename_img_file_all.append(basename_img_file)
                for s in data_keys_json:
                    if basename_img_file in s:
                        matching = s
    #find IMG name and replace with basename
                        if data [matching]['filename'] == file:
                            data [matching]['filename'] = basename
                            number_matches_json_allimg =number_matches_json_allimg+1                 
                        #chang data_keys of json file 
                        split_data_keys_json = os.path.splitext(matching)
                        #add and join
                        data_keys_json_new = split_data_keys_json[0]+get_name_from_copied_folder+split_data_keys_json[1]
    #                    d['test2'] = d.pop('test')
                        data[data_keys_json_new]=data.pop(matching)                   
            else:
                no_match = no_match + 1
                print('no match in json')
                print(file +'  file')

if change_json == True:
    with open(path_json_edit, 'w') as fp:
        json.dump(data, fp)