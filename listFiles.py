import os

#set target directory
target_dir = input("Enter the path to the directory you want to create a tree from: ")

#list everything inside target_dir

dir_tree = {}

for dirpath, dirnames, files in os.walk(target_dir):
    # print(f'Found directory: {dirpath}')
    temp_index = []
    for file_name in files:
        if file_name.endswith(".md"):
            temp_index.append(file_name)
    if len(temp_index) >0:
        dir_tree.update({dirpath : temp_index})

print("Directory Tree:")
print(dir_tree)