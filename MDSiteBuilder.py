from create_dir_tree import create_dir_tree
from make_HTML import make_html
import os
from make_index import make_index
from make_css import make_css

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
    
    #replace source dir with save_dir in subdir path
    new_path = subdir.replace(target, save_dir)
    
    #create save_dir/subdir_name if it doesn't already exist
    try:
        os.scandir(new_path)
    except:
        os.mkdir(new_path)

    for entry in tree[subdir]:
        #print(entry)
        if entry.endswith(".md"):
            #needs full filepath
            make_html(f"{subdir}/{entry}",new_path)
            # print(f"Converted {subdir}/{entry} to HTML")

#generate index.html and style.css

make_index(target, save_dir)

make_css(save_dir)