import os

#set target directory
target_dir = "./testDir"

#list everything inside target_dir
for dirpath, dirnames, files in os.walk(target_dir):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
