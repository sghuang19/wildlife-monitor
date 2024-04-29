from ultralytics import YOLO
import os
from sys import stderr

from config import PT_PATH, CLASSES

print("[INFO] Initializing object detection model")

# Fetching the pre-trained weights
if not os.path.exists("yolov8n.pt"):
    print(f"[INFO] Downloading the pre-trained weights from {PT_PATH}")
    if os.system(f"wget {PT_PATH}") != 0:
        print("[ERROR] Failed to download the pre-trained weights", file=stderr)
        exit(1)
    print("[INFO] Pre-trained weights downloaded")

# Initialize the model
model = YOLO("yolov8n.pt")

print("[INFO] Model loaded")


def detect(image):
    # image can be either a path or a PIL object
    print("[INFO] Start detection")
    result = model(image)
    print("[INFO] Detection completed")
    return result


def compare(results):
    result = results[0]  # keep the first
    classes = set()
    for cls in result.boxes.cls:  # get boxes detected
        name = result.names[cls.item()]  # get name of the class
        if name in CLASSES:
            classes.add(name)
    return classes
