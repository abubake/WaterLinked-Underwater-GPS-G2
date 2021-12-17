import os
import numpy as np
import cv2
from glob import glob

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, gap=6):
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0
    
    # Set time stamp initial values #########################################################

    YYYYMMDD = 20211201 # Set the year, month, and day here
    hh = 11 # Set the starting hour here (0 to 23)
    mm = 52 # Set the starting minute here
    ss = 0 # Set the starting second here
    ddd = 0 # Set the starting 100th of a second here, please enter in increments of 100
    # EX.) 100, or 200, 300, etc. up to 900
    
    # Every frame extracted is a 1/10 of a second. Code is designed to only handle this rate.
    # Future work could enable any extraction rate desired
    # Generating correct time steps depends on the gap variable, paired with the minimum value
    # ddd imcrements at, which is "+100" each 6 frames for a frame rate of 60 fps
    
    #########################################################################################
    
    if hh < 10:
        hh_string = "0" + str(hh)
    else:
        hh_string = str(hh)           
    if mm < 10:
        mm_string = "0" + str(mm)
    else:
        mm_string = str(mm)             
    if ss < 10:
        ss_string = "0" + str(ss)
    else:
        ss_string = str(ss)           
    if ddd == 0:
        ddd_string = "00" + str(ddd)
    else:
        ddd_string = str(ddd)
                
    timeStamp = hh_string + mm_string + ss_string + ddd_string
    frame_name = "M116" + "_" + str(YYYYMMDD) + "_" + timeStamp + "_" + "img" + str(idx)

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break
        
        if idx == 0:
            cv2.imwrite(f"{save_path}/{frame_name}.JPEG", frame)
            
        else:
            
            if idx % gap == 0:
                
                ddd += 100
                
                if ddd == 1000:
                    ddd = 0
                    ss += 1
                    if ss == 60:
                        ss = 0
                        mm += 1
                        if mm == 60:
                            mm = 0
                            hh += 1
                            if hh == 24:
                                hh = 0
                
                if hh < 10:
                    hh_string = "0" + str(hh)
                else:
                    hh_string = str(hh)
                    
                if mm < 10:
                    mm_string = "0" + str(mm)
                else:
                    mm_string = str(mm)   
                    
                if ss < 10:
                    ss_string = "0" + str(ss)
                else:
                    ss_string = str(ss) 
                    
                if ddd == 0:
                    ddd_string = "00" + str(ddd)
                else:
                    ddd_string = str(ddd)  
                    
                timeStamp = hh_string + mm_string + ss_string + ddd_string
                frame_name = "M116" + "_" + str(YYYYMMDD) + "_" + timeStamp + "_" + "img" + str(idx)   
                cv2.imwrite(f"{save_path}/{frame_name}.JPEG", frame)

        idx += 1

if __name__ == "__main__":
    video_paths = glob("C:/Users/baker/Desktop/videos/*")
    save_dir = "C:/Users/baker/Desktop/save"

    for path in video_paths:
        save_frame(path, save_dir, gap=6)