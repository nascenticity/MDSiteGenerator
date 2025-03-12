# import markdown for converting markdown to html strings
from markdown import *

def make_html(some_file):
    
#get file contents & convert to html
    with open (some_file, "r") as f:

        text = f.read()
        output = markdown(text)

    #print (output)

    pageTitle = "Hello World"

    html_template = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{pageTitle}</title> <link rel="stylesheet" href="style.css"> </head><body>{output}</body></html>'

    #create new filename
    file_name = some_file.removesuffix(".md")
    print(file_name)
    with open(f"{file_name}.html", "w") as f2:
        f2.write(html_template)

#make_html("./testDir/testMD.md")