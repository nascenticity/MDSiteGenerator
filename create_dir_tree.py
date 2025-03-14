import os



#set target directory
#target_dir = input("Enter the path to the directory you want to create a tree from: ")

#list everything inside target_dir
def create_dir_tree(target_dir):

    #empty dictionary object to contain directory tree info
    dir_tree = {}

    # walk the target directory & index all md files & subdirectories containing md files
    for dirpath, dirnames, files in os.walk(target_dir):
        # print(f'Found directory: {dirpath}')
        #array to hold file names while in given subdirectory
        
        #removes root directory from path
        pathy = dirpath.removeprefix(target_dir)
        print(pathy)
        

        temp_index = []
        for file_name in files:
            # filter out files in hidden directories
            if not pathy.startswith("/."):
                temp_index.append(file_name)
        if len(temp_index) >0:
            #add a dictionary containing the subdirectory path & array of all md files within
            dir_tree.update({dirpath : temp_index})

    #with open("dir_tree.txt", "w") as f:
    #    f.write("Directory Tree: \n")
     #   for subdir in dir_tree:
      #      f.write(f"{subdir} \n")
       #     for entry in dir_tree[subdir]:
        #        f.write(f"- {entry} \n")
    
    return dir_tree

#create_dir_tree(input("Enter the path to the directory you want to create a tree from: "))