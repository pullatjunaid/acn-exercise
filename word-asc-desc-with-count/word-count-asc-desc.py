import os.path
from os import path

fileName=""
sortedListWithCount=[]
def countTexts():
    global count
    file=open(fileName, "rb")
    with file as f:
        fileData=f.read().decode()
        words=fileData.split()
        # print(words)
        sortedList=words
        sortedList.sort()

        uniqueArray=[]
        for word in sortedList:
            if word not in uniqueArray: 
                uniqueArray.append(word)
                    
        # print(uniqueArray)
        for item in uniqueArray:
            count=0
            for item2 in words:
                if item2.lower()==item.lower():
                    count=count+1
            sortedListWithCount.append({'text':item,'count':count})
        # print(sortedListWithCount)

        for wd in sortedListWithCount:
            print(wd['text'],"-",wd['count'])

fileName=input(str("Enter file name: "))
if os.path.exists(fileName):
    print("File exists")
    countTexts()
else:
    print("File does not exists")
