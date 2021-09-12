import os.path
from os import path

fileName=""
count=0
def countTexts():
    global count
    file=open(fileName, "rb")
    wordToCount=input(str("Enter word to count: "))
    with file as f:
        fileData=f.read().decode()
        words=fileData.split()
        for word in words:
            if word.lower()==wordToCount.lower():
                count=count+1

        print("The word",wordToCount,"is occuring",count,"times")

fileName=input(str("Enter file name: "))
if os.path.exists(fileName):
    print("File exists")
    countTexts()
else:
    print("File does not exists")
