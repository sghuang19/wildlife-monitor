from ultralytics import YOLO
import os
import config

global model


def model_init():
    # Fetching the pre-trained weights
    if not os.path.exists("yolov8n.pt"):
        print(
            f"[INFO] Downloading the pre-trained weights from "
            f"{config.PT_PATH}")
        if os.system(f"wget {config.PT_PATH}") != 0:
            print("[ERROR] Failed to download the pre-trained weights",
                  file=sys.stderr)
            exit(1)

    # Initialize the model
    global model
    model = YOLO("yolov8n.pt")


def detect(image):
    # image can be either a path or a PIL object
    global model
    return model(image)


def compare(results):
    result = results[0]  # keep the first
    classes = set()
    for cls in result.boxes.cls:  # get boxes detected
        name = result.names[cls.item()]  # get name of the class
        if name in config.CLASSES:
            classes.add(name)
    return classes


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        path = "https://http.cat/404.jpg"  # use default image if not provided
    else:
        path = sys.argv[1]
    model_init()
    results = detect(path)
    classes = compare(results)
    print(classes)
