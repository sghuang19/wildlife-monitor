from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request

import os
import tempfile
import time
from cv2 import imencode

import config

print("[INFO] Initializing Google Drive API")

enabled = True
SCOPES = ['https://www.googleapis.com/auth/drive.file']

credentials = Credentials.from_service_account_file(config.KEY_FILE,
                                                    scopes=SCOPES)
if not credentials:
    print("[ERROR] Failed to retrieve credentials.")
    enabled = False
try:
    credentials.refresh(Request())
except RefreshError as e:
    print("[ERROR] Failed to refresh credentials:", e)
    enabled = False

if not enabled:
    print("[ERROR] Errors occurred, Google Drive upload will be disabled.")
else:
    service = build('drive', 'v3', credentials=credentials)
    print("[INFO] Google Drive API initialized")


def upload(image):
    print("[INFO] Uploading captured image to Google Drive")
    file_name = f"{time.time()}.jpg"
    # TODO: readable file name

    image_bytes = imencode('.jpg', image)[1].tobytes()
    file_metadata = {'name': file_name, 'parents': [config.FOLDER_ID]}

    with tempfile.NamedTemporaryFile(suffix='.jpg') as temp_file:
        temp_file.write(image_bytes)
        temp_file_name = temp_file.name
        media_body = MediaFileUpload(temp_file_name, mimetype='image/png')

        try:
            file = service.files().create(body=file_metadata,
                                          media_body=media_body,
                                          fields='id').execute()
            print('[INFO] File ID:', file.get('id'))
            print('[INFO] Image uploaded to Google Drive')
        except Exception as e:
            print("[ERROR] An error occurred while uploading the image:", e)
