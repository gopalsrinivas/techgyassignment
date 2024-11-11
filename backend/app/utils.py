import os
import time
from typing import List, Union
from fastapi import UploadFile
from dotenv import load_dotenv

load_dotenv()

MEDIA_FOLDER = os.getenv(
    "MEDIA_FOLDER", "D:/Projects/Task/techgyassignment/backend/media")

if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)


def save_files(files: List[UploadFile], folder_name: str) -> Union[List[str], None]:
    if not files:
        return None

    saved_paths = []
    for file in files:
        if file.filename: 
            unique_id = str(int(time.time() * 1000))
            filename = f"{unique_id}_{file.filename}"

            file_path = os.path.join(MEDIA_FOLDER, folder_name, filename)
            folder_path = os.path.dirname(file_path)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

 
            with open(file_path, "wb") as buffer:
                buffer.write(file.file.read())

            saved_paths.append(filename)

    return saved_paths if saved_paths else None
