import requests
import os

user = os.path.expanduser("~")
directory = os.path.join(user, "supplier-data", "images")
files = os.listdir(directory)
url = "http://35.184.254.88/upload/"

def upload_images(files):
    for file in files:
        if file.endswith(".jpeg"):
            with open(directory + "/" + file, "rb") as opened:
                r = requests.post(url, files={'file': opened})
                r.raise_for_status()
                print("Successfully uploaded the image!")

upload_images(files)
