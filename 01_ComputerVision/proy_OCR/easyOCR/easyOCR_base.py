'''
inference and cropping of images

'''
import easyocr
import cv2
import numpy as np
from pathlib import Path   # To work with abs paths
import os


# Define easyOCR instance
reader = easyocr.Reader(['en'], False, verbose = False)  # language, GPU

# Define paths
folder = r'imgs\logos\various_03_03_22'

for i,img_name in enumerate(os.listdir(folder)):
    img_path = Path(os.path.join(folder, img_name)).as_posix()
    head_tail = os.path.split(img_path)
    if img_path.endswith(('jpg', 'png', 'jpeg')):
        # Read image
        img = cv2.imread(img_path)
        imgCopy = img.copy()

        # easyOCR --> object: Read image 
        result = reader.readtext(img)

        # Plot the bounding boxes
        for detection in result: 
            # Extract coordinates
            xmin, ymin = detection[0][0]
            xmax, ymax = detection[0][2]
            text = detection[1]
            # Plot
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.rectangle(imgCopy,(int(xmin), int(ymin)),(int(xmax), int(ymax)),(0,255,0),3)
            cv2.putText(imgCopy,text,(int(xmin), int(ymin)),font,1,(0,0,255),2,cv2.LINE_AA)
        
        

        # Path to save image
        output_path = os.path.join(head_tail[0], 'output', 'OUT_' + head_tail[1])
        
        # Check if output folder exists
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))
        # Save image
        cv2.imwrite(output_path,imgCopy)  
        print(f'Next image {i+1}')








