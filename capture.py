from cv2 import VideoCapture


def capture():
    print("[INFO] Capturing image")
    retval = False
    cam = VideoCapture(0)
    retval, frame = cam.read()
    if not retval:
        print("[ERROR] Failed to capture a frame, aborting")
    else:
        print("[INFO] Frame captured")
    cam.release()
    return frame
