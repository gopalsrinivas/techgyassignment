import os
from typing import List
from fastapi import UploadFile

# Specify the media folder path where the files will be saved
MEDIA_FOLDER = "D:/Projects/Task/techgyassignment/backend/media"

# Ensure the media folder exists
if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)

def save_files(files: List[UploadFile], folder_name: str) -> List[str]:
    saved_paths = []
    for file in files:
        file_path = os.path.join(MEDIA_FOLDER, folder_name, file.filename)
        folder_path = os.path.dirname(file_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Save the file
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        saved_paths.append(file_path)

    return saved_paths
