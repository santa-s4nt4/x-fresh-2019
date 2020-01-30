import os
import glob

files = glob.glob(
    "C:\\Users\\santa\\Desktop\\Python\\x-fresh\\dataDrivenArt\\bin\\data\\images\\*.jpg")
for i, old_name in enumerate(files):
    new_name = "C:\\Users\\santa\\Desktop\\Python\\x-fresh\\dataDrivenArt\\bin\\data\\images\\{0:04d}.jpg".format(
        i + 1)
    os.rename(old_name, new_name)
    print(old_name + " -> " + new_name)
