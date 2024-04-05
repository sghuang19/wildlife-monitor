import config
import os
import urllib.parse


def message(classes):
    # create a message
    return f"Animals detected: {', '.join(classes)}"


def notify(msg):
    if os.system(f"curl \"{config.NOTIFY_API}{urllib.parse.quote(msg)}\""):
        print(f"Failed to send message: {msg}")
    else:
        print(f"Message sent: {msg}")


if __name__ == "__main__":
    msg = message({"cat", "dog"})
    notify(msg)

