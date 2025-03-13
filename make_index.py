# import markdown for converting markdown to html strings
from markdown import *
from bs4 import BeautifulSoup
import os

def make_index(source_dir, destination):

    
    try:
        # check if README.html has been created at destination
        os.scandir(f"{destination}/README.html")
        
        #move the contents of README.html to index.html and delete README.html  
        with open(f"{destination}/README.html", "r") as f:
            content = f.read()
            content = BeautifulSoup(content)
        
        with open(f"{destination}/index.html", "w") as f2:
            f2.write(content.prettify())
        
        os.remove(f"{destination}/README.html")
    except:
        # if not, create a blank index.html file
        with open(f"{destination}/index.html", "w") as f3:
            f3.write("")   
    
        

                  
   
   
