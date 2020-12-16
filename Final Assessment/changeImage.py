from PIL import Image
import os

user = os.path.expanduser("~")
directory = os.path.join(user, "supplier-data", "images")
files = os.listdir(directory)

def update_images(files):
  for file in files:
    try:
      file_name = os.path.splitext(file)[0]
      im = Image.open(os.path.join(directory, file))
      im.resize((600,400)).convert("RGB").save(directory + "/" + file_name + ".jpeg")
    except OSError:
      continue

update_images(files)





