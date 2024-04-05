from subprocess import Popen, PIPE
from PIL import Image
from io import BytesIO

def capture():
    # Run fswebcam command to capture image
    command = "fswebcam -"
    process = Popen(command.split(), stdout=PIPE)
    output, _ = process.communicate()

    # Convert output to PIL Image
    image = Image.open(BytesIO(output))

    return image

