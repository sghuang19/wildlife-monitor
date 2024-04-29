from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
from io import BytesIO
from PIL import Image
import tempfile
import time
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request

def upload_gd(image_data, service_account_key_file, folder_id):
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    credentials = Credentials.from_service_account_file(service_account_key_file, scopes=SCOPES)

    if not credentials:
        print("Failed to retrieve credentials.")
        return

    try:
        credentials.refresh(Request())
    except RefreshError as e:
        print("Failed to refresh credentials:", e)
        return

    service = build('drive', 'v3', credentials=credentials)
    file_name = str(time.time()) + '.png'

    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        temp_file.write(image_data)
        temp_file_name = temp_file.name

    media_body = MediaFileUpload(temp_file_name, mimetype='image/png', resumable=True)
    file_metadata = {'name': file_name, 'parents': [folder_id]}  # Set the folder ID here

    try:
        file = service.files().create(body=file_metadata, media_body=media_body, fields='id').execute()
        print('File ID:', file.get('id'))
    except Exception as e:
        print("An error occurred while uploading the file:", e)
    finally:
        os.unlink(temp_file_name)  # Ensure the temporary file is deleted after upload

if __name__ == "__main__":
    with open("nerd.png", "rb") as image_file:
        image_data = image_file.read()

    service_account_key_file = "credentials.json"
    folder_id = "1ENyRMNshsWLZKDLs9wYskuWU1pl-2Gkr"  # Replace with your actual folder ID
    upload_gd(image_data, service_account_key_file, folder_id)

