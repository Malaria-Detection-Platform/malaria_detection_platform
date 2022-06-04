#crop the largest parasite from each image and save it. requires orginal image and associated binary mask
from django.conf import settings
import cv2 
import os
import numpy as np
from cv2 import boxPoints
from tqdm import tqdm

def savecrop(original_img, original_file_name, output_directory, x,y,w,h, window_h, window_w):
    
    extension=".png"
    max_h= window_h # should be 224
    max_w= window_w # should be 224
    delta_h=max_h-h
    delta_w=max_w-w
    
    #position center
    a=y-(delta_h // 2)
    b=y-(delta_h // 2)+max_h
    e=x-(delta_w // 2)
    f=x-(delta_w // 2)+max_w    
    if a>=0 and b<=original_img.shape[0] and e>=0 and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2) 
        return
        
    
        
    #position 4 middle left
    a=y-(delta_h // 2)
    b=a+max_h
    e=x
    f=e+max_w     
    if a>=0 and b<=original_img.shape[0] and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)
        return
    
    #position 6 middle right
    a=y-(delta_h // 2)
    b=a+max_h
    e=x-delta_w
    f=e+max_w    
    if a>=0 and b<=original_img.shape[0] and e>=0 and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)
        return

    
    #position 2 up center
    a=y
    b=y+max_h
    e=x-(delta_w // 2)
    f=x-(delta_w // 2)+max_w      
    if e>=0 and b<=original_img.shape[0] and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)
        return
    
    #position 1 up left
    a=y
    b=y+max_h
    e=x
    f=x+max_w        
    if b<=original_img.shape[0] and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)
        return
    
    #position 3 up right
    a=y
    b=y+max_h
    e=x-delta_w
    f=x-delta_w+max_w      
    if b<=original_img.shape[0] and e>=0 and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)
        return
    
    #position 8 down center
    a=y-delta_h
    b=a+max_h
    e=x-(delta_w // 2)
    f=e+max_w   
    if a>=0 and b<=original_img.shape[0] and e>=0 and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)
        return
    
    #position 7 down left
    a=y-delta_h
    b=a+max_h
    e=x
    f=e+max_w   
    if a>=0 and b<=original_img.shape[0] and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)
        return   
            
    #position 9 down right
    a=y-delta_h
    b=a+max_h
    e=x-delta_w
    f=e+max_w  
    if a>=0 and b<=original_img.shape[0] and e>=0 and f<=original_img.shape[1]:
        
        new_img2=original_img[a:b,e:f]#img
        #writes the new file in the Crops folder
        new_name = original_file_name.split(extension, 1)[0]
        full_path_file_name = os.path.join(output_directory, new_name +".png")
        cv2.imwrite(full_path_file_name, new_img2)


def crop_largest(gray_img,color_img, original_file_name, output_directory):
    
    (cnts, _) = cv2.findContours(gray_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)
    
    gray_rgb = cv2.cvtColor(gray_img, cv2.COLOR_BGR2RGB)
    #print("{}{}".format('Detected parasites: ',len(c)))
    if (len(c)>0):
        max_area = 0
        index_max=-1
        flag = 0
        for i in range(0,len(c)):
            x, y, w, h = cv2.boundingRect(c[i])
            if((w*h > max_area)): #50176 and (w*h <= 50176)
                index_max = i
                max_area = w*h
                flag = 1
        
        if(flag == 1):
            x,y,w,h = cv2.boundingRect(c[index_max])
            savecrop(color_img, original_file_name, output_directory, x,y,w,h, 224, 224)
    else:
        fn.append(original_file_name)
        
def crop():        

    mask_directory = os.path.join(settings.BASE_DIR,'media','predict')
    original_directory = os.path.join(settings.BASE_DIR,'media','img')
    output = os.path.join(settings.BASE_DIR,'media','crops')

    extension = ".png"
    #gt_file_list = os.listdir(gt_directory)
    original_file_list = os.listdir(original_directory)
    fn=[]
    for original_file_name in tqdm(original_file_list):
    
        #mask images reading and binary thresholding
        prefix_name = original_file_name.split(extension, 1)
        mask_file_name = prefix_name[0] +extension
    
        mask_path = os.path.join(mask_directory, mask_file_name)
        mask_img= cv2.imread(mask_path, 0) # 0 for grayscale flag
        #gt_img=cv2.cvtColor(gt_img, cv2.COLOR_BGR2GRAY)
        (thresh, mask_img) = cv2.threshold(mask_img, 127, 255, cv2.THRESH_BINARY)
    
        #original image reading
        original_path = os.path.join(original_directory, original_file_name)
        original_img= cv2.imread(original_path)
    
        #crop largest parasite if it exists
        crop_largest(mask_img,original_img,original_file_name, output)
    
    print("List of images without parasites: %s" % fn)