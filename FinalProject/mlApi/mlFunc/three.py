#parasite contours delineation on original image, number of parasites is saved within the name of the image
import cv2 
import numpy as np
from cv2 import boxPoints
import os
from tqdm import tqdm
from django.conf import settings


def box_fun(gray_img,color_img):
    (cnts, _) = cv2.findContours(gray_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)
    gray_rgb = cv2.cvtColor(gray_img, cv2.COLOR_BGR2RGB)
    #print("{}{}".format('Detected parasites: ',len(c)))
    for i in range(0,len(c)):
        #use the 2 statement to trace boxes and replace c[i] by box
        #rect = cv2.minAreaRect(c[i])
        #box =  np.int0(boxPoints(rect))
        cv2.drawContours(color_img, [c[i]], -1, (0, 0, 255), 3) 
        
    return len(c), color_img 


def contours():

    # images and mask directories
    img_directory = os.path.join(settings.BASE_DIR,'media','img')
    mask_directory = os.path.join(settings.BASE_DIR,'media','predict')

    # contours output directory
    original_bb_directory = os.path.join(settings.BASE_DIR,'media','contours')

    #gt_file_list = os.listdir(gt_directory)
    original_file_list = os.listdir(img_directory)

    for original_file_name in tqdm(original_file_list):
    
        #mask images reading and binary thresholding
        mask_path = os.path.join(mask_directory, original_file_name)
        mask_img= cv2.imread(mask_path, 0) # 0 for grayscale flag
        (thresh, mask_img) = cv2.threshold(mask_img, 127, 255, cv2.THRESH_BINARY)
    
        #original image reading
        original_path = os.path.join(img_directory, original_file_name)
        original_img= cv2.imread(original_path)
    
        #parasite counting for each image and contour tracing
        parasite_count, original_img_bound = box_fun(mask_img,original_img)
    
        #save original img with boxes
        new_name = original_file_name.split(".png", 1)
        new_name = os.path.join(original_bb_directory, new_name[0]+"_"+str(parasite_count)+"_parasites.png")
        cv2.imwrite(new_name, original_img_bound)
        return new_name
    
    
    