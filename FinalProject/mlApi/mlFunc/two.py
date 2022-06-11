# Binary mask resize to original image size 
import cv2
import numpy as np
import os 
from tqdm import tqdm
from django.conf import settings


def resize_function(input_directory, output_directory, new_w, new_h):
    
    original_file_list = os.listdir(input_directory)
    
    for img_file in tqdm(original_file_list):
        
        # read gt image in binary format
        full_path = os.path.join(input_directory, img_file)
        mask= cv2.imread(full_path, 0) # 0 for grayscale flag
        (thresh, mask) = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        
        #resize
        dsize = (new_w,new_h)
        # resize image
        mask = cv2.resize(mask, dsize)
        (thresh, mask) = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        
        # copy and paste original image
        full_path = os.path.join(output_directory, img_file)
        cv2.imwrite(full_path, mask)

def maskresize():


    input_directory = os.path.join(settings.BASE_DIR,"media","predict")
    output_directory= os.path.join(settings.BASE_DIR,"media","predict")

#dataset1
#new_w = 2592
#new_h = 1944

#dataset2
    new_w = 1382
    new_h = 1030

    resize_function(input_directory, output_directory, new_w, new_h)