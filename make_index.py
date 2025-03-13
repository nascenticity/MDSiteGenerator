# import markdown for converting markdown to html strings
from markdown import *
from bs4 import BeautifulSoup
import os

def make_index(source_dir, destination):

    try:
        os.scandir(f"{source_dir}/README.md")
    except:
        with open(f"{source_dir}/README.md", "w") as r:
            r.write("")
 
    
    #convert README.md file to temp html file
    markdownFromFile(
        input= f"{source_dir}/README.md",
        output=f'{destination}/index.html',
        encoding='utf8',
    )
    
    #convert links referencing .md files & replace references with the equivalent .html files
    with open(f"{destination}/index.html", "r+") as f:
        contents = f.read()
        contents = contents.replace(".md",".html")
        #resetting to the 0th character in the file is necessary to force contents to be overwritten
        f.seek(0)
        f.write(contents)

    #read temp html back in using Beautiful Soup
    with open(f"{destination}/index.html", "r") as f2:
        temp_html = BeautifulSoup(f2.read())

    #print(temp_html)

    #generate template as BeautifulSoup object
    with open("./template.html", "r") as t:
       html_template = BeautifulSoup(t.read())

    #insert converted html output into template
    main = html_template.select_one('main')
    #but only if there is any converted html to insert
    if len(temp_html) > 0:
        main.append(temp_html)
   
    #change page heading to be consistent with file name
    title = html_template.select_one('title')
    title.append(input("Enter the name of your webpage: "))

    with open(f"{destination}/index.html", "w") as f3:
        f3.write(f"{html_template.prettify()}")
