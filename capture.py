from cv2 import VideoCapture
from time import sleep


def capture():
    retval = False
    cam = VideoCapture(0)
    retval, frame = cam.read()
    if not retval:
        print("[ERROR] Failed to capture a frame, aborting")
    cam.release()
    return frame

