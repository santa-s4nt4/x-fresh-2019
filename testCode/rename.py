import os
import glob

files = glob.glob("../dataDrivenArt/bin/data/images/*.jpg")
for i, old_name in enumerate(files):
    new_name = "../dataDrivenArt/bin/data/images/{0:01d}.jpg".format(i + 1)
    os.rename(old_name, new_name)
    print(old_name + " -> " + new_name)
