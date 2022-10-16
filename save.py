from PIL import ImageGrab   #pip install image
import cv2  #pip install opencv-ptyhon
import numpy as np  #pip install numpy 
import keyboard #pip install keyboard
import time     #pip install time


x = 0

def TakeSsAndSave():
    screenshot = np.array(ImageGrab.grab(bbox=(640,220,1280,860)))
    screenshot = cv2.cvtColor(screenshot,cv2.COLOR_BGR2RGB)
    cv2.imwrite(file_name , screenshot)
    
    

while(True):
    try:
        if keyboard.is_pressed('u'):
            time.sleep(1)
            file_name = str(x) + ".jpg"
            TakeSsAndSave()   
            x = x + 1
            
    except:
        break