file = input('Enter file name: ')

def get_tags(content):
    flag = False
    word = ''
    tags = []
    for letter in content:
        if(letter == '<' and not(flag)):
            word = word + letter
            flag = True
        elif((letter != '>' and letter != ' ') and flag):
            word = word + letter
        elif((letter == '>' or letter == ' ') and flag):
            word = word + '>'
            tags.append(word)
            word = ''
            flag = False
    return tags

with open(file, 'r') as file:
    contents = file.read().lower()
    tags = get_tags(contents)
    
    for tag in tags:
        if tag[1] != '/':
            print(tag)