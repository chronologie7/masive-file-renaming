#!/usr/bin/env python3

import os, re

regex = r"(file)(_)(\d+)(\.\w+)"
fileList = os.walk(".", topdown=False)

for root, dirs, files in fileList:
    for file in files:
        try:
            re_result = re.findall(regex, file)
            source = os.path.join(root, file)
            newName = re_result[0][0] + re_result[0][2] + re_result[0][3]
            newName = os.path.join(root, newName)
            print(f"renaming: {source}...")
            os.rename(source, newName)
        except:
            continue
print("done!")
