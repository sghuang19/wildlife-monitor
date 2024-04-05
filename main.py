import capture
import detect
import notify
import time

if __name__ == "__main__":
    detect.init()
    while True:
        image = capture.capture()
        results = detect.detect(image)
        print(results)
        classes = detect.compare(results)
        msg = notify.message(classes)
        notify.notify(msg)
        time.sleep(1)

