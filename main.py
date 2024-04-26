from capture import *
from detect import *
from notify import *
from motion import *

from time import sleep
from threading import Thread

pressed = False


def check_input():
    global pressed
    input()
    pressed = True


model_init()
pir = pir_init()

while True:
    if not pir.available():
        continue

    if pir.object_detected():
        print("[INFO] Object detected")
        print("[INFO] Waiting 5 seconds for stabilization")
        sleep(5)

        print("[INFO] Start detection")
        image = capture()
        results = detect(image)
        print(results)
        classes = compare(results)
        msg = message(classes)
        notify(msg)
        print("[INFO] Notification sent")

        # TODO: upload captured images to cloud

        print("[INFO] Suspend system for 60 secs, press any key to resume")
        thread = Thread(target=check_input)
        thread.start()
        while not pressed:
            sleep(1)
        thread.join()
        print("[INFO] System resumed")

    if pir.object_removed():
        print("[INFO] Object Removed")
    pir.clear_event_bits()
    sleep(0.2)
