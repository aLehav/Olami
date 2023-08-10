import urllib.request
import zipfile
import os
import shutil

def extract_zip_text(url,
                 ignored_files=["README.txt"],
                 temp_zip_name="temp.zip",
                 temp_zip_path="temp"):
    # Download the zip file
    urllib.request.urlretrieve(url, temp_zip_name)

    text = ""
    # Open the zip file
    with zipfile.ZipFile(temp_zip_name, "r") as zip_file:
        # Go to the zip subdirectory
        if os.path.exists(temp_zip_path):
            shutil.rmtree(temp_zip_path)
        zip_file.extractall(temp_zip_path)
        text_path = os.path.join(temp_zip_path, os.listdir(temp_zip_path)[0])
        for file_name in os.listdir(text_path):
            if file_name not in ignored_files:
                with open(text_path + '/' + file_name) as f:
                    text += f.read() + "\n"
    shutil.rmtree(temp_zip_path)
    os.remove(temp_zip_name)
    return text