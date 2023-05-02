import os
from opencc import OpenCC

trans = OpenCC("s2tw")  # simple chinese to tranditional chinese
files_name = files = os.listdir(os.curdir)
for item in files_name:
    if item != "toCHT.py":  # and item != ""#other files name isn't need to translate
        filename_arr = item.split(".", 1)
        new_filename = filename_arr[0] + "_CHT." + filename_arr[1]
        print(new_filename)
        newfile = open(new_filename, "w+", encoding="utf-8")
        f = open(item, "r", encoding="utf-8")
        for line in f.readlines():
            transLine = trans.convert(line)
            print(transLine)
            newfile.write(transLine)
        newfile.close()
