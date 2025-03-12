from create_dir_tree import create_dir_tree
from make_HTML import make_html


target = input("Enter the path to the directory: ")

# create a list of files to convert
tree = create_dir_tree(target)

#convert each file
for subdir in tree:
    #print(subdir)
    for entry in tree[subdir]:
        #print(entry)
        if entry.endswith(".md"):
            #needs full filepath
            make_html(f"{subdir}/{entry}")
            print(f"Converted {subdir}/{entry} to HTML")

#generate index.html and style.css
with open(f"{target}/index.html", "w") as f2:
    f2.write("")

with open(f"{target}/style.css", "w") as f3:
    f3.write("")