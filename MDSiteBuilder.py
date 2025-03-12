from create_dir_tree import create_dir_tree
from make_HTML import make_html

# create a list of files to convert
target = input("Enter the path to the directory: ")

tree = create_dir_tree(target)

for subdir in tree:
    #print(subdir)
    for entry in tree[subdir]:
        #print(entry)
        if entry.endswith(".md"):
            #needs full filepath
            make_html(f"{subdir}/{entry}")
            print(f"Converted {subdir}/{entry} to HTML")