import os, re

regex = r"(file)(_)(\d+)(\.txt)"
fileList = os.walk(".", topdown=False)

for root, dirs, files in fileList:
    for file in files:
        try:
            re_result = re.findall(regex, file)
            source = root + "\\" + file
            newName = root + "\\" + re_result[0][0] + re_result[0][2] + re_result[0][3]
            print(f"renaming: \"{root}\\{file}...")
            os.rename(source, newName)
        except:
            continue
print("done!")
