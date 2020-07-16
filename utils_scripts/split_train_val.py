# -*- coding: utf-8 -*-
"""
Split one dataset to trainig and validation
Created on Sat Jun 20 14:45:00 2020

@author: sven
"""
# Merge two or more VIA2 projects
#
# Author: Abhishek Dutta <adutta@robots.ox.ac.uk>
# Date: 18 May 2020

import json
import numpy as np
import shutil
import os


#%%
#change here!!
copy_img = False #True
copy_json = True
train_prop = 0.75 # todo [0:73]
#%%
# add the filename of all VIA2 projects
# Note: all VIA projects should have same attributes and project settings
root_project_path =r'E:\Datasets_GGU_Bodenproben\Bodenproben_recognition\snipped_img\Soil_Classification' #'C:\Users\sven\Desktop\Masterthesis\github\data\vgg_annotation\img_horizontal\new_train_02'
all_img_json_folder = 'dataset_train_till_IMG_5203BKF 38_4' #'all_img_train_val_and_json'
# load json of all images
filename = os.path.join(root_project_path,all_img_json_folder,'changed_json_soiltype_id.json') #via_project_merged.json')
# copy attributes and other project settings from one of the projects
# assumption: all the projects have same attributes and settings
via2 = {}
with open(filename, 'r') as f:
  via2 = json.load(f)
 
  #%%
data_keys_json = list(via2.keys()) 
#seperate json
data_keys_json_train = data_keys_json[0: int(train_prop * np.size(data_keys_json))]
data_keys_json_val = data_keys_json[int(train_prop * np.size(data_keys_json)):]
via2_train = dict((k,via2[k]) for k in data_keys_json_train)
via2_val = dict((k,via2[k]) for k in data_keys_json_val)

#copy images to train and val folder

# define the name of the directory to be created
path_train = os.path.join(root_project_path,'train')
path_val = os.path.join(root_project_path,'val')

if not os.path.exists(path_train):
    os.mkdir(path_train)
if not os.path.exists(path_val):       
    os.mkdir(path_val)
    
if copy_img:
    for i in data_keys_json_train:
        img_filename_train = via2_train[i]['filename'] 
        src = os.path.join(root_project_path,all_img_json_folder,img_filename_train)
        dst = os.path.join(path_train,all_img_json_folder,img_filename_train)
        shutil.copy(src,path_train)
    for i in data_keys_json_val:
        img_filename_val = via2_val[i]['filename']
        src = os.path.join(root_project_path,all_img_json_folder,img_filename_val)
        dst = os.path.join(path_train,img_filename_val)
        shutil.copy(src,path_val)
        
if copy_json:
    output_filename_train = os.path.join(path_train,'via_train.json')
    with open(output_filename_train, 'w') as fout_train:
      json.dump(via2_train, fout_train)
if copy_json:
    output_filename_val = os.path.join(path_val,'via_val.json')
    with open(output_filename_val, 'w') as fout_val:
      json.dump(via2_val, fout_val)

