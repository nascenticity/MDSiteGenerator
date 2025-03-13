# import markdown for converting markdown to html strings
from markdown import *
from bs4 import BeautifulSoup
import os

def make_index(destination):

    #generate template as BeautifulSoup object
    with open("./template.html", "r") as t:
       html_template = BeautifulSoup(t.read())
   
    #change page heading to be consistent with project
    title = html_template.select_one('title')
    title.append(input("Enter a name for your webpage: "))

    with open(f"{destination}/index.html", "w") as f3:
        f3.write(f"{html_template.prettify()}")

#make_html("./testDir/subDir/testMD2.md")