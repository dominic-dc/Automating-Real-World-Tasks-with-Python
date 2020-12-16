import os
import requests

user = os.path.expanduser("~")
directory = os.path.join(user, "supplier-data", "descriptions")
files = os.listdir(directory)

def process(files):
    for file in files:
        json_data = {}
        with open(directory + "/" + file) as txt:
            lines = txt.readlines()
            json_data["name"] = lines[0].strip()
            weight = lines[1].strip().split()
            json_data["weight"] = int(weight[0])
            json_data["description"] = lines[2].strip()
            image = os.path.splitext(file)[0]
            json_data["image_name"] = image + '.jpeg'
        print(json_data)
        upload_to_website(json_data)

def upload_to_website(json_data):
    p = json_data
    r = requests.post("http://35.184.254.88/fruits/", json=p)
    r.raise_for_status()
    print("Successfully uploaded data!")

process(files)
