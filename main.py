import capture
import detect
import time

if __name__ == "__main__":
    detect.init()
    while True:
        image = capture.capture()
        results = detect(image)
        print(results)
        compare(results)
        time.sleep(1)

