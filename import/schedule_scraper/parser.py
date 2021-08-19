from bs4 import BeautifulSoup

months_list = ["december", "january", "february", "march", "april", "may", "june", "july"]

for month in months_list:
    with open("{}.html".format(month), "r") as html_file:
        html = BeautifulSoup(html_file, "html.parser")

    raw_schedule = html.find(id="div_schedule")
    
# tags of interest "toi"
urls = [tag.find("a")["href"] for tag in html.find_all(attrs={"data-stat": "box_score_text"}, scope=False) if len(tag.contents) == 1]

with open("urls.txt", "a+") as url_file:
    url_file.write("\n".join(urls))
    
