import os

#set target directory
target_dir = "./testDir"

#list everything inside target_dir

dir_tree = {}

for dirpath, dirnames, files in os.walk(target_dir):
    print(f'Found directory: {dirpath}')
    dir_tree.update({dirpath : files})
    for file_name in files:
        print(file_name)
        

print("Directory Tree:")
print(dir_tree)