import streamlit as st
import cv2
import numpy as np


class OpError(Exception):
    pass


class VideoMotion:
    def __init__(self, history, path, kernel_size=(3, 3)):
        self.history = history
        self.path = path
        self.kernel_size= kernel_size
        
    def validate_video(self):
        video = cv2.VideoCapture(self.path)
        if not video.isOpened():
            raise OpError("Cannot find the correct patyh to the video, try it again.")
        return video
        
    def motion_detection(self):
        knn = cv2.createBackgroundSubtractorKNN(history=self.history)
        
        color_frame_ = "Color Frames"
        binary_frame_ = "Binary Frames"
        
        cv2.namedWindow(color_frame_)
        cv2.namedWindow(binary_frame_)
        
        video = self.validate_video()
        
        while True:
            ok, frame = video.read()
            
            if not ok:
                break
            
            binary_frame = knn.apply(frame)
            eroded_frame = cv2.erode(binary_frame, np.ones(self.kernel_size, np.uint8))
            find_non_zeros = cv2.findNonZero(eroded_frame)
            x, y, xw, yh = cv2.boundingRect(find_non_zeros)
            
            if find_non_zeros is not None:
                cv2.rectangle(frame, (x, y), (x + xw, y + yh), (0, 0, 255), 4)
                
            color_frame = cv2.cvtColor(eroded_frame, cv2.COLOR_GRAY2RGB)
            
            cv2.imshow(color_frame_, frame)
            cv2.imshow(binary_frame_, color_frame)
            
            key = cv2.waitKey(1)
            
            if key == ord("Q") or key == ord("q") or key == 27:
                break
            
        video.release()
        cv2.destroyAllWindows()