# Wildlife Camera with Raspberry Pi

A course project for [CSE 40373 Embedded System
Development](https://github.com/adstriegel/cse40373-sp24) at the University of
Notre Dame.

Group members include:

- Steven Baranko ([@StevenBaranko](https://github.com/SteveBaranko)):
  [sbaranko@nd.edu](mailto://sbaranko@nd.edu)
- Samuel Huang ([@sghuang19](https://github.com/sghuang19)):
  [ghuang3@nd.edu](mailto://ghuang3@nd.edu)

This project implements a system to detect and classify animals with a
combination of motion sensor, webcam,
[YOLOv8](https://github.com/ultralytics/ultralytics) model, send a notification
to user's smartphone, and upload the captured image to Google Drive.

The system has a modular design:

- `config.py`: Configurations of this app.
- `main.py`: Entry point of this app.
- `motion.py`: Initialization of PIR motion sensor.
- `capture.py`: Utilities for capturing frames from video device, e.g. a
  webcam.
- `detect.py`: Feed the frame captured into image detection model.
- `notify.py`: Send notification to the user's smartphone using
  [Bark](https://github.com/Finb/Bark).
- `upload.py`: Upload the captured image to Google Drive through API.

To try this app, you will need to create your own **Google Drive API
credential**, **folder ID**, and **Bark API address**. The API keys in the
source code will be deprecated when this repo is made public.

