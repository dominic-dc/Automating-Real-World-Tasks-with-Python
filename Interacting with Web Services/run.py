import os
import requests

path_to_files = "/data/feedback"
files = os.listdir(path_to_files)
ip_add = "34.122.6.192"

def process(files):
    for file in files:
        content = {}
        with open(path_to_files + "/" + file) as txt:
            lines = txt.readlines()
            content["title"] = lines[0].strip()
            content["name"] = lines[1].strip()
            content["date"] = lines[2].strip()
            content["feedback"] = lines[3].strip()
        upload_to_website(content)


def upload_to_website(feedbacks):
    p = feedbacks
    response = requests.post('http://34.122.6.192/feedback', data=p)
    response.raise_for_status()
    print("Successfully processed the request!")

process(files)

