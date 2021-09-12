import os.path 
from os import path

filename=""
inputText=""
newText=""
file=""
is_text_found=False

def checkIsWordExists():
    global file
    with file as f:
        datafiles=f.readlines()
        for line in datafiles:
            if inputText in line.decode(): 
                global is_text_found
                is_text_found=True 

        if is_text_found==True:
            newText=input(str("Enter new text: "))
            file=open(filename, 'rb')
            fileData=file.read()
            # update text 
            updatedFile=fileData.decode().replace(inputText, newText) 
            # Enter new file name 
            newFileName=input('Enter new file name: ')
            newfile=open(newFileName,'wb')
            newfile.write(updatedFile.encode())
            file.close()
            print('\n  ',inputText,'is replaced with',newText, 'and saved to new file: ',newFileName)
            exit()
        else:
            print('The word', inputText, "does not exists in this file") 

def getTexts(): 
    global inputText, newText
    inputText=input("Enter text to replace: ")
    checkIsWordExists()

# get word file 
filename=input("Enter word file name: ")
if os.path.exists(filename):
    print('File exists')
    file=open(filename, 'rb')
    getTexts()
else:
    print("File not exists!")
    exit()




