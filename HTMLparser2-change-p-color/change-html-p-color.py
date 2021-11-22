import os.path
from os import path
from os import write

def changeColor():
    pclr = input("Enter second paragraph color: ")
    newData = ""

    with open(htmlfilename) as htmlf:
        # print(htmlf.read())
        readedFile = htmlf.read()
        for i, p in enumerate(readedFile.split('\n\n'), start=0):
            if (i == 1):
                nwp = p.replace("color: black", "color: " + pclr)
                newData += nwp
            else:
                newData += p

    # print(newData)
    newfilename = input("Ente new file name: ")
    nwf = open(newfilename, "w")
    nwf.write(newData)
    print("Paragraph color changed and saved to new file with name: "+newfilename)

htmlfilename = input("Enter HTML file name: ")
if os.path.exists(htmlfilename):
    print('File exists')
    changeColor()
else:
    print("File not exists")