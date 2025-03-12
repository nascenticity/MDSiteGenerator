# import markdown for converting markdown to html strings
from markdown import *

def make_html(some_file):
    
#get file contents & convert to html
    with open (some_file, "r") as f:

        #read file & store contents in text variable
        text = f.read()

        #if text contains any links targeting md files, alter them to target the equivalent html file instead
        
        text = text.replace(".md", ".html")

        #convert text to markdown & store in output variable
        output = markdown(text)

    #print (output)

    pageTitle = "Hello World"

    html_template = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{pageTitle}</title> <link rel="stylesheet" href="style.css"> </head><body><nav><a href="/index.html">{pageTitle}</a></nav>{output}</body></html>'

    #create new filename
    file_name = some_file.removesuffix(".md")
    print(file_name)
    with open(f"{file_name}.html", "w") as f2:
        f2.write(html_template)

make_html("./testDir/subDir/testMD2.md")