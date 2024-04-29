from os import system
from sys import stderr
from urllib import parse

from config import NOTIFY_API


def message(classes):
    # create a message
    return f"Animals detected: {', '.join(classes)}"


def notify(msg):
    print("[INFO] Sending notification")
    if system(f"curl \"{NOTIFY_API}{parse.quote(msg)}\""):
        print(f"[ERROR] Failed to send message: {msg}", file=stderr)
    else:
        print(f"[INFO] Message sent: {msg}")


if __name__ == "__main__":
    # test cases
    msg = message({"cat", "dog"})
    notify(msg)
