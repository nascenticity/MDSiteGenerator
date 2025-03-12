# get contents of md files & use them to generate a corresponding html file

with open('testMD.md', 'r') as mdFile:
    with open('testMD.html', 'w') as htmlFile:
        for line in mdFile:
            htmlFile.write(line)
    