from html.parser import HTMLParser

# filename=input(str("Enter html file name: "))
filename="sample.html"
openedFile=open(filename,"rb")

class NewHtmlParser(HTMLParser):
    print
    def handle_starttag(self, tag, attrs):
        print('hi')
        print(tag)

with openedFile as f:
    print(type(f.read().decode()))


    parser=NewHtmlParser()
    parser.feed(f.read().decode())