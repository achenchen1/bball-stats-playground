from bs4 import BeautifulSoup

with open("202012220BRK.html", "r") as html_file:
    html = BeautifulSoup(html_file, "html.parser")

# tags of interest "toi"
urls = html.find_all(attrs={"data-stat": "player"})

with open("test.txt", "a+") as url_file:
    url_file.write("\n".join(urls))
    
