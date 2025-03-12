# get contents of md files & use them to generate a corresponding html file

with open('test.md', 'r') as mdFile:
    with open('test.html', 'w') as htmlFile:
        for line in mdFile:
            htmlFile.write(line)
    