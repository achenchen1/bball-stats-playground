from html.parser import HTMLParser

my_set = set()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        my_set.add(data)

parser = MyHTMLParser()

with open("output_1.html", "r") as f:
    html_output = f.read()

parser.feed(html_output)

for x in my_set:
    print(x)
