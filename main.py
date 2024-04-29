from capture import *
from detect import *
from notify import *
from motion import *
from upload import *

from time import sleep
from threading import Thread

pressed = False


def check_input():
    global pressed
    input()
    pressed = True


print("[INFO] Initializing PIR sensor")
pir = pir_init()
print("[INFO] PIR sensor initialized")

while True:
    if not pir.available():
        continue

    if pir.object_detected():
        print("[INFO] Object detected")
        print("[INFO] Waiting 5 seconds for stabilization")
        sleep(5)

        print("[INFO] Capturing image")
        image = capture()
        if image is None:
            continue
        print("[INFO] Image captured")

        print("[INFO] Start detection")
        results = detect(image)
        print("[INFO] Detection completed")
        classes = compare(results)
        if not classes:
            print("[INFO] No animals detected")
            continue
        print(f"[INFO] Animals detected: {', '.join(classes)}")

        print("[INFO] Sending notification")
        msg = message(classes)
        notify(msg)
        print("[INFO] Notification sent")

        print("[INFO] Uploading captured image to Google Drive")
        upload_gd(image, "credentials.json", "1ENyRMNshsWLZKDLs9wYskuWU1pl-2Gkr")
        print("[INFO] Image uploaded")

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
