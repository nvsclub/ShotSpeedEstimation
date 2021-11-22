# This script uses opencv2 to visualize a video.
# Press F to go back one frame
# Press G to go forward one frame
# Press H to go forward 300 frames
# Press S to register the frame number

import cv2
import numpy as np

# Change these 2 variables to setup the video
video_name = 'data/video/raw/NORM0061.mp4'
frame_offset = 31245
# Increase the backlog limit to have more margin to go back (or decrease to reduce memory consumption)
backlog_limit = 100
targets = np.array([0])

cap = cv2.VideoCapture(video_name)

if (cap.isOpened()== False):
    print("Error opening video stream or file")
    exit(0)

frame_number = 0
frame_backlog = []
current_frame = 0
debit_frames = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    frame_number += 1

    if frame_offset > 0:
        frame_offset -= 1
        continue

    if ret == True:
        # Adding frame counter to the video, remove this line to remove it
        cv2.putText(frame, str(frame_number), (0,100), 0, 5, (0,0,0), thickness=5)
        
        if debit_frames <= 1:
            cv2.imshow('Frame', frame)

        frame_backlog.append(frame)
        current_frame = -1
        debit_frames -= 1

        while True and debit_frames <= 0:
            control = cv2.waitKey(10000)
            
            if control == ord('s'):
                # We save the frame number in the save_points file for later use
                save_points = open('data/save_points.txt', 'a')
                save_points.write(f'{video_name}: {frame_number + current_frame + 1}\n')
                save_points.close()
            elif control == ord('f'):
                if current_frame - 1 > - len(frame_backlog):
                    current_frame -= 1
                cv2.imshow('Frame', frame_backlog[current_frame])
            elif control == ord('g'):
                current_frame += 1
                if current_frame == 0:
                    break
                cv2.imshow('Frame', frame_backlog[current_frame])
            elif control == ord('h'):
                debit_frames = 300
            elif control == ord('n'): 
                debit_frames = targets[targets > (frame_number + current_frame + 1)].min() - (frame_number + current_frame + 1)

            # Add extra key pressing functions here if you wish

        frame_backlog = frame_backlog[-backlog_limit:]

    
    # Break the loop
    elif ret != True:
        break
