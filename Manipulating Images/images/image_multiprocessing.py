from PIL import Image
import os
from multiprocessing import Pool

parent_dir = os.getcwd()
directory = os.path.join("opt", "icons")

if not os.path.exists(directory):
    os.mkdir("opt")
    os.chdir("opt")
    os.mkdir("icons")
    os.chdir("..")

def operate(file):
        try:
            name = os.path.splitext(file)[0]
            outfile = os.path.join(parent_dir, directory, name)
            im = Image.open(os.path.join(parent_dir, "images", file))
            im.rotate(90).resize((128,128)).convert("RGB").save(outfile + ".jpeg")
        except OSError as e:
            print(e)

# This script utilizes the multiprocessing module to improve the overall performance 
# during runtime of the script. Specifically, it uses Pool to determine the number
# of tasks that will be done repeatedly in the function operate().
# By using the parallel processing, each task will be executed simultaneously
# in multiple processors of the computer itself.
 
if __name__ == "__main__":
    files = os.listdir("images")
    p = Pool(len(files))
    p.map(operate, files)
