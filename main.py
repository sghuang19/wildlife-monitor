from detect import detect, compare
from motion import pir
from upload import upload
from capture import capture
from notify import message, notify

from time import sleep
from threading import Thread

pressed = False


def check_input():
    global pressed
    input()
    pressed = True


while True:
    if not pir.available():
        continue

    if pir.object_detected():
        print("[INFO] Object detected")
        print("[INFO] Waiting 5 seconds for stabilization")
        sleep(5)

        image = capture()
        if image is None:
            continue

        results = detect(image)
        classes = compare(results)
        if not classes:
            print("[INFO] No animals detected")
            continue
        print(f"[INFO] Animals detected: {', '.join(classes)}")

        msg = message(classes)
        notify(msg)

        upload(image)

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
    sleep(1)
