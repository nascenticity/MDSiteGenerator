# import markdown for converting markdown to html strings
from markdown import *
from bs4 import BeautifulSoup
import os
from markdown.extensions.tables import TableExtension

def make_html(some_file, destination):

    #remove .md suffix from filepath, split filepath at /, isolate filename, & 
    filepath = some_file.removesuffix(".md")
    split_name = filepath.rsplit("/")
    file_name = split_name[-1]
   
    #convert md file to temp html file
    markdownFromFile(
        input= some_file,
        output=f"{destination}/{file_name}.html",
        encoding='utf8',
        extensions=[TableExtension(use_align_attribute=True)]
    )
    
    #convert links referencing .md files & replace references with the equivalent .html files
    with open(f"{destination}/{file_name}.html", "r+") as f:
        contents = f.read()
        contents = contents.replace(".md",".html")
        #resetting to the 0th character in the file is necessary to force contents to be overwritten
        f.seek(0)
        f.write(contents)

    #read temp html back in using Beautiful Soup
    with open(f"{destination}/{file_name}.html", "r") as f2:
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
    title.append(file_name)

    #add page header containing site name
    header = html_template.select_one("header")
    header.append(file_name)

    with open(f"{destination}/{file_name}.html", "w") as f3:
        f3.seek( 0 )
        f3.write(f"{html_template.prettify()}")

