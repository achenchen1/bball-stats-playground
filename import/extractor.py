from bs4 import BeautifulSoup

class Team:
    def __init__(tag):
        self.full_name = tag.contents[0]
        self.location = tag.contents[0].rsplit(maxsplit=1)[0]
        self.name = tag.contents[0].split()[-1]
        self.abbreviation = tag["href"].split("/")[-2]

# [<a href="/teams/MIL/2021.html" itemprop="name">Milwaukee Bucks</a>, <a href="/teams/BRK/2021.html" itemprop="name">Brooklyn Nets</a>]

def single_game(file_name):
    ot = False
    team_a = None
    team_b = None

    with open(file_name, "r") as f:
        html = BeautifulSoup(f, "html.parser")

    tbody = html.find_all("tbody")
    ot = len(tbody) > 16
    team_a_data = tbody[:len(tbody)//2]
    team_b_data = tbody[len(tbody)//2:]

    # The team_a_tables now has all the information we want. Roughly, we have:
    # team_a_tables = [FullBoxScore, Q1, Q2, H1, Q3, Q4, (OT1, OT2, ...), AdvancedBoxScore]
    # team_b_tables = [FullBoxScore, Q1, Q2, H1, Q3, Q4, (OT1, OT2, ...), AdvancedBoxScore]
    team_a_tables = [table.find_all("tr", class_=None) for table in team_a_data]
    team_b_tables = [table.find_all("tr", class_=None) for table in team_b_data]
    x = html.find_all("a", itemprop="name")
    for i in x:
        print(i.contents[0])
        print(i.contents[0].rsplit(maxsplit=1)[0])
        print(i["href"].split("/")[-2])

    for x in team_a_tables[0]:
        b = x.find_all("td")
        for y in b:
            print(y.string)
    

single_game("game_htmls/202012220BRK.html")

# for x in team_a_tables:
#   b = x.find_all("td")
#   for y in b:
#       y.string

