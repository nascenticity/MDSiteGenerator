from create_dir_tree import create_dir_tree

# create a list of files to convert
target = input("Enter the path to the directory: ")

tree = create_dir_tree(target)

for subdir in tree:
    print(subdir)
    for entry in tree[subdir]:
        print(entry)