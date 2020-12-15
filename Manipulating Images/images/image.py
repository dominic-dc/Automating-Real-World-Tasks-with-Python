from PIL import Image
import os

parent_dir = os.getcwd()
print("Current working directory:", os.getcwd())
directory = os.path.join("opt", "icons")

if not os.path.exists(directory):
    os.mkdir("opt")
    os.chdir("opt")
    os.mkdir("icons")
    os.chdir("..")
    
files = os.listdir("images")


def operate(files):
    for file in files:
        try:
            name = os.path.splitext(file)[0]
            outfile = os.path.join(parent_dir, directory, name)
            im = Image.open(os.path.join(parent_dir, "images", file))
            im.rotate(90).resize((128,128)).convert("RGB").save(outfile + ".jpeg")
        except OSError:
            continue

operate(files)