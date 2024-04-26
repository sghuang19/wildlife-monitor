import config
import os
import urllib.parse
from sys import stderr


def message(classes):
    # create a message
    return f"[INFO] Animals detected: {', '.join(classes)}"


def notify(msg):
    if os.system(f"curl \"{config.NOTIFY_API}{urllib.parse.quote(msg)}\""):
        print(f"[ERROR] Failed to send message: {msg}", file=stderr)
    else:
        print(f"[INFO] Message sent: {msg}")


if __name__ == "__main__":
    msg = message({"cat", "dog"})
    notify(msg)
