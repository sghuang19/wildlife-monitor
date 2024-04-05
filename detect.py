from ultralytics import YOLO
import os
import config


def init():
    # Fetching the pre-trained weights
    if not os.path.exists("yolov8n.pt"):
        print(f"Downloading the pre-trained weights from {config.PT_PATH}")
        if os.system(f"wget {config.PT_PATH}") != 0:
            print("Failed to download the pre-trained weights")
            exit(1)

    # Initialize the model
    global model
    model = YOLO("yolov8n.pt")


def detect(path):
    global model
    return model(path)


def compare(results):
    result = results[0]  # keep the first
    classes = set()
    for cls in result.boxes.cls:  # get boxes detected
        name = result.names[cls.item()]  # get name of the class
        if name in config.CLASSES:
            classes.add(name)
    print(classes)
    # TODO: invoke the notify function


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        path = "https://http.cat/404.jpg"  # use default image if not provided
    else:
        path = sys.argv[1]
    init()
    results = detect(path)
    compare(results)

