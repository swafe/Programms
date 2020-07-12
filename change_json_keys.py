# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:52:15 2020

@author: sven
script to change key in json to rfere regions from one json to other images

"""

import shutil
import os

import numpy as np
import json 

from PIL import Image, ImageDraw
#%%
def get_access_to_json(image_path):
  image_name = os.path.splitext(os.path.basename(image_path))[0]
  filename = os.path.basename(image_path)
  img_size =  os.path.getsize(image_path)
  filename_and_size = filename + str(img_size)
  return filename_and_size, filename
#%%

# Python program to read json file 
# change here !!!!!!
path_data = r'E:\Datasets_GGU_Bodenproben\Bodenproben_recognition\snipped_img\Soil_Classification\dataset_train_till_IMG_5203BKF 38_4'
json_name = 'via_project_10Jul2020_12h16m_json(14).json'  #'via_project_merged.json'
json_file_dir = os.path.join(path_data, json_name)     
     
# Opening JSON file 
f = open(json_file_dir) 
# returns JSON object as a dictionary 
data_01 = json.load(f) 
# Closing file 
f.close()   
    
#%%
new_json_path = path_data # r'E:\Datasets_GGU_Bodenproben\Bodenproben_recognition\snipped_img\snipped_ohne_sign_all'
json_name_regions_and_sign = 'changed_json.json'
json_file_dir_region_and_sign = os.path.join(new_json_path, json_name_regions_and_sign) 

#get all images in path_test_dir
image_paths = []
for filename in sorted(os.listdir(new_json_path), key=str.lower):
    if os.path.splitext(filename)[1].lower() in ['.png', '.jpg', '.jpeg']:
      image_paths.append(os.path.join(new_json_path, filename))
      
data_new = data_01
for path_i in image_paths:
    filename_and_size, filename = get_access_to_json(path_i) 
    print(filename_and_size)
    data_keys_json = list(data_new.keys())#['IMG_0332.JPG1076716']
    #            basename_img_file_all.append(basename_img_file)
    for s in data_keys_json:
        if filename in s:
            matching = s    
            data_new[filename_and_size]=data_new.pop(matching)

# save annotation as json
if True:
    with open(json_file_dir_region_and_sign, 'w') as fp_new:
        json.dump(data_new, fp_new)   
    
    
    
    
    
    
    
