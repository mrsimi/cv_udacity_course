import os
import glob 
import matplotlib.image as mpimg
import cv2



def load_dataset(image_dir):
    img_list = []
    img_types = ['day', 'night']
    
    for img_type in img_types:
        
        for file in glob.glob(os.path.join(image_dir, img_type, '*')):
            img = mpimg.imread(file)
            
            if not img is None:
                img_list.append((img, img_type))
                
    
    return img_list


def standardize_image(image):
    std_img=  cv2.resize(image, (1110, 600))   
    return std_img

def encode_label(label):
    if label== 'day':
        return 1
    else:
        return 0

def standardize_inputs(img_list):
    std_list = []
    
    for img in img_list:
        std_img = standardize_image(img[0])
        std_label = encode_label(img[1])
        
        std_list.append((std_img, std_label))
    
    return std_list            