from motion import  VideoMotion

history = 350
path = 1
kernel_size = (5, 5)

video = VideoMotion(history=history, path=path, kernel_size=kernel_size)

video.motion_detection()