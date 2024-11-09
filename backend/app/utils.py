import os
import time
from typing import List, Union
from fastapi import UploadFile
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Specify the media folder path from an environment variable
MEDIA_FOLDER = os.getenv("MEDIA_FOLDER", "D:/Projects/Task/techgyassignment/backend/media")

# Ensure the media folder exists
if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)


def save_files(files: List[UploadFile], folder_name: str) -> Union[List[str], None]:
    if not files:
        # Return None if no files are provided
        return None

    saved_paths = []
    for file in files:
        if file.filename:  # Ensure file has a name
            # Add unique identifier to the file name
            unique_id = str(int(time.time() * 1000))
            filename = f"{unique_id}_{file.filename}"

            # Construct file path
            file_path = os.path.join(MEDIA_FOLDER, folder_name, filename)
            folder_path = os.path.dirname(file_path)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Save the file
            with open(file_path, "wb") as buffer:
                buffer.write(file.file.read())

            saved_paths.append(filename)

    # Return saved file paths only if there are files
    return saved_paths if saved_paths else None
