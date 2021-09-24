# file = input('Enter file name: ')
file ="sample.html"

def get_tags(content):
    flag = False
    word = ''
    tags = []
    tag = ''
    attributes=[]
    attrWord=''
    isAttribute = False
    parsedList=[]

    for letter in content:
        if(letter == '<' and not(flag)):
            word = word + letter
            flag = True
            # tag=''
        elif(letter ==' ' and flag):
            word = word + '>'
            tags.append(word)
            word = ''
            flag = False
            # Attributes starts 
            isAttribute = True
        elif (letter!=' ' and letter!='>' and isAttribute):
            attrWord=attrWord+letter
        elif (isAttribute and letter==' '):
            attributes.append(attrWord)
        elif(isAttribute and letter=='>'):
            word = word + '>'
            tags.append(word)
            flag = False
            # tag=word
            print(tag,'nnnnnnn')
            attributes.append(attrWord)
            obj={
                'tag':tag,
                'attr':attributes
            }
            parsedList.append(obj)
            attributes=[]
            attrWord=''
            word = ''
            isAttribute=False
            tag=''

        elif((letter != '>' and letter != ' ') and flag):
            word = word + letter
        elif((letter == '>' or letter == ' ') and flag):
            word = word + '>'
            tag= word
            tags.append(word)
            word = ''
            flag = False
            
    print(attributes)
    print(parsedList)
    return tags

with open(file, 'r') as file:
    contents = file.read().lower()
    tags = get_tags(contents)
    
    for tag in tags:
        if tag[1] != '/':
            print(tag)