import os
from bs4 import BeautifulSoup

def make_css(save_dir):
    # copy template.css to style.css
    with open("./template.css", "r") as t:
        style = t.read()

    with open(f"{save_dir}/style.css", "w") as f:
        f.write(style)

    print(save_dir)

    #iterating thru the contents of save_dir
    for dirpath, dirnames, files in os.walk(save_dir):

        for file_name in files:

            #select html files
            if file_name.endswith(".html"):
                #print(dirpath)
                #print(file_name)

                where_css = os.path.relpath(f"{save_dir}/style.css", dirpath)

                #print(where_css)

                with open(f"{dirpath}/{file_name}", "r") as f:
                    contents = f.read()
                    contents = BeautifulSoup(contents)

                if len(contents) > 0:
                    stylesheet = contents.select_one("link")
                    stylesheet["href"] = where_css
                    #print(stylesheet)
                    with open(f"{dirpath}/{file_name}", "w") as f2:
                        f2.write(f"{contents}")
    
