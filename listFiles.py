import os

#set target directory
target_dir = "./testDir"

#list everything inside target_dir
dirList = os.scandir(target_dir)
for entry in dirList:
    print(entry.name)
