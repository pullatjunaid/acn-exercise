

def check():
    filename= input(str("Please enter file name: "))
    file=open(filename,'rb')

    searchText=input(str("Enter text to search: "))

    print(searchText)
    is_text_found=False
    with file as f:
        datafiles=f.readlines()
        for line in datafiles:
            if searchText in line.decode():
                is_text_found=True
        if is_text_found==True:
             print('The word ', searchText, " is included in the file") 
        else:
                print('The word ', searchText, " is not included in the file") 


check()