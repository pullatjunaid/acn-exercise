# file = input('Enter file name: ')
file ="sample.html"

def get_tags(content):
    tag=''
    attributes=[]
    attribute=''
    is_tag_started=False
    is_end_started=False
    parsedList=[]

    for letter in content:
        if(letter=='<' and not is_tag_started):
            tag=''
            tag=tag+letter
            is_tag_started=True
        elif(letter=='>' and not is_end_started):
            tag=tag+'>'
            parsedList.append({
                'tag':tag
            })
            is_tag_started=False
            tag=''  
        elif(letter=='>' and is_end_started):
            is_tag_started=False
            tag=''  
            is_end_started=False
        elif(letter=="/"):
            tag=''
            is_tag_started=False
            is_end_started=True
        elif(letter!='<' and letter!='>' and letter!=' '):
            tag=tag+letter

    print(parsedList)    

with open(file, 'r') as file:
    contents = file.read().lower()
    tags = get_tags(contents)
    
  