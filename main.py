import cv2 as cv
import numpy as np
import os
from time import sleep, time
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
import torch
import cv2
import numpy as np
import subprocess
from mss import mss



model = torch.hub.load(r'C:\Users\user\Projects\project\test\yolov5-master', 'custom', path=r'C:\Users\user\Projects\project\test\best.pt', source='local')
wincap = WindowCapture('Seal Online Plus')

with mss() as sct:
    while(True):
        screenshot = wincap.get_screenshot()
        results = model(screenshot, size=640)

        df= results.pandas().xyxy[0]

        try:
            xmin = int(df.iloc[0,0])
            ymin = int(df.iloc[0,1])
            xmax = int(df.iloc[0,2])
            ymax = int(df.iloc[0,3])
            
            cv2.rectangle(screenshot, (xmin, ymin), (xmax, ymax), (255,0,0), 2)
        except:
            print("",end="")

        cv2.imshow("frame", screenshot)
        
        if(cv2.waitKey(1) == ord('q')):
            cv2.destroyAllWindows()
            break

# wincap = WindowCapture('Seal Online Plus')

# while(True):
#     screenshot = wincap.get_screenshot()
#     mana_50 = screenshot[53, 188]
#     print(mana_50[0], mana_50[1], mana_50[2])

#     # if mana_50 != [172 202 226]:
#     #     subprocess.run('function\mana_f2.amk',  shell=True, check=True)

#     # print(screenshot[196, 57]) 
#     cv2.imshow("frame", screenshot)

#     if(cv2.waitKey(1) == ord('q')):
#         cv2.destroyAllWindows()
#         break