# import tinyhtml for creating html elements, and markdown for converting markdown to html strings
# from tinyhtml import *
from markdown import *

#get file contents & convert to html
with open ("testMD.md", "r") as f:

    text = f.read()
    output = markdown(text)

print (output)

# use tinyhtml to create an empty html template
# html_content = html(lang="en")(
  #  h("head")(
   #     h("meta", charset="utf-8")
    #),
    # h("body")(
      # frag(output)
    # ),
#)
#print(html_content.render()) 

pageTitle = "Hello World"

html_template = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{pageTitle}</title> <link rel="stylesheet" href="style.css"> </head><body>{output}</body></html>'

with open("testMD.html", "w") as f2:
    f2.write(html_template)
