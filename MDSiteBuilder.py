from create_dir_tree import create_dir_tree
from make_HTML import make_html
import os
from make_index import make_index

target = input("Enter the path to the directory: ")
save_dir = input("Enter the path to the location where you want to save the html files: ")

#create the destination directory if it doesn't exist
try:
    os.scandir(save_dir)
except:
    os.mkdir(save_dir)
   
#create the destination directory if it doesn't already exist

# create a list of files to convert
tree = create_dir_tree(target)

#convert each file
for subdir in tree:
    #print(subdir)
    for entry in tree[subdir]:
        #print(entry)
        if entry.endswith(".md"):
            #needs full filepath
            make_html(f"{subdir}/{entry}",save_dir)
            print(f"Converted {subdir}/{entry} to HTML")

#generate index.html and style.css

make_index(save_dir)

with open(f"{save_dir}/style.css", "w") as f3:
    f3.write("")