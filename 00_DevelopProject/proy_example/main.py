# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
'''
*Description:*\n
\t This script is an example of the usage of the  XXXX project for the YYYY.\n
\t It is used to extract the information from the images. By the use of 2 internal modules:\n
\t\t - module_A --> ....]\n
\t\t - module_B--> M....\n

# Folder Structure

    Project/
    |
    └── lib/
        |
        |
        ├── module_A/
        |   |
        |   ├── *imgs/
        |   |     └──imgtest.jpg 
        |   ├── *tmp/
        |   |     └──debug.jpg 
        |   |     
        |   └── script_1.py
        |   |
        |   └── sript_2.py
        |   |
        |   └── script_4.py
        |   
        |
        └── module_B/
            |   
            ├──  script_1.py
            |   
            ├──  moduleB_1/
            |   |
            |   |
            |   ├── module_B11/*
            |   |
            |   └── module_B12/
            |   
            └──  module_B2/
                |
                └── module_B21/
                    |
                    └── ttttt.json



'''

# Modulesfrom pathlib import Path                              # work with directories
from module_A.module_A1.script_A import function_A             #
from module_B.module_B1.script_B import function_B        
from module_B.module_B2.module_B21 import function_C                 
# from tqdm import tqdm                                                        



if __name__ == '__main__':

    # Parameters
    sssss   = 'R13'               # display type
    pppp = False                  # debug mode

    # CALIBRATOR    -----------------------------------------------------------------------------------------------------  

    
    # CAMERA MODULE -----------------------------------------------------------------------------------------------------   
    cam = function_A(sssss, pppp)               # initialize camera module
    cam.setup()                                 # setup camera
    img_path = cam.captureFrame()               # Capture an image and get image path
    cam.closeCam()                              # Close the camera

    # OCR MODULE ---------------------------------------------------------------------------------------------------------
    # # Initialize OCR module
    OCR = function_B(dispositive, debug)       # Initialize the class
    OCR.loadOCRTech()                          # Load the OCR tech method asked
    metadata = OCR.getText(img_path)           # Extract the information from the image and get the metadata from the requested id

    print(metadata)




    

    

   


    
   
    
    
    

    

   
