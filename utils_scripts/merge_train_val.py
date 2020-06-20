# -*- coding: utf-8 -*-
"""
Split one dataset to trainig and validation
Created on Sat Jun 20 14:45:00 2020
from: https://gitlab.com/vgg/via/-/blob/master/via-2.x.y/scripts/io/merge_via2_projects.py
@author: sven
"""
# Merge two or more VIA2 projects
#
# Author: Abhishek Dutta <adutta@robots.ox.ac.uk>
# Date: 18 May 2020

import json

# add the filename of all VIA2 projects
# Note: all VIA projects should have same attributes and project settings
filename_list = [r'C:\Users\sven\Desktop\Masterthesis\github\data\vgg_annotation\img_horizontal\project_9091\all_img_and_json\recognice_sample_train_5205_horiz.json', r'C:\Users\sven\Desktop\Masterthesis\github\data\vgg_annotation\img_horizontal\project_9091\all_img_and_json\recognice_sample_val_5206_5272_horiz.json']
output_filename = r'C:\Users\sven\Desktop\Masterthesis\github\data\vgg_annotation\img_horizontal\project_9091\all_img_and_json\via_project_merged.json'

# copy attributes and other project settings from one of the projects
# assumption: all the projects have same attributes and settings
via2 = {}
with open(filename_list[0], 'r') as f:
  via2 = json.load(f)

discarded_count = 0
for i in range(1, len(filename_list)):
  with open(filename_list[i], 'r') as f:
    pdata_i = json.load(f)
    for metadata_i in pdata_i:
      # check if a metadata already exists
      if metadata_i not in via2:
        via2[metadata_i] = pdata_i[metadata_i]
      else:
        discarded_count = discarded_count + 1

with open(output_filename, 'w') as fout:
  json.dump(via2, fout)
print('Written merged project to %s (discarded %d metadata)' % (output_filename, discarded_count))

