# import markdown for converting markdown to html strings
from markdown import *

#get file contents & convert to html
with open ("testMD.md", "r") as f:

    text = f.read()
    output = markdown(text)

print (output)

pageTitle = "Hello World"

html_template = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{pageTitle}</title> <link rel="stylesheet" href="style.css"> </head><body>{output}</body></html>'

with open("testMD.html", "w") as f2:
    f2.write(html_template)
