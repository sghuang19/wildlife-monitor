from cv2 import VideoCapture
from time import sleep

def capture():
    cam = VideoCapture(0)
    retval = False
    while True:
        retval, frame = cam.read()
        if not retval:
            print("Failed to capture a frame, retrying")
            sleep(1)
        else:
            return frame

