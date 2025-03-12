# import tinyhtml for creating html elements, and markdown for converting markdown to html strings
from tinyhtml import *
from markdown import *

#get file contents & convert to html
with open ("testMD.md", "r") as f:

    text = f.read()
    output = markdown(text)

print (output)

# use tinyhtml to create an empty html template
html_content = html(lang="en")(
    h("head")(),
    h("body")(
       output
    ),
)
print(html_content.render()) 
