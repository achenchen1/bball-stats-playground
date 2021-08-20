from bs4 import BeautifulSoup

class Team:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.players = []

class BoxScoreBasic:
    def __init__(self, stats_list):
        self.stats = {}
        self.stats["mp"] = next(stats_list)
        self.stats["fg"] = next(stats_list)
        self.stats["fga"] = next(stats_list)
        self.stats["fgpt"] = next(stats_list)
        self.stats["tpm"] = next(stats_list)
        self.stats["tpa"] = next(stats_list)
        self.stats["ft"] = next(stats_list)
        self.stats["fta"] = next(stats_list)
        self.stats["orb"] = next(stats_list)
        self.stats["drb"] = next(stats_list)
        self.stats["trb"] = next(stats_list)
        self.stats["ast"] = next(stats_list)
        self.stats["stl"] = next(stats_list)
        self.stats["blk"] = next(stats_list)
        self.stats["tov"] = next(stats_list)
        self.stats["pf"] = next(stats_list)
        self.stats["pts"] = next(stats_list)
        self.stats["pm"] = next(stats_list)
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
    team_names = html.find_all("a", itemprop="name")

    team_a = Team(team_names[0].contents[0], team_names[0]["href"].split("/")[-2])
    team_b = Team(team_names[1].contents[0], team_names[1]["href"].split("/")[-2])

    player_stats = []
    for row in team_a_tables[0]:
        player_stats.append(BoxScoreBasic(tag.string for tag in row.find_all("td")))

    for stat in player_stats:
        print(stat.stats)

    for x in team_a_tables[0]:
        b = x.find_all("td")
        for y in b:
            print(y.string, end=" | ")
        print("")

single_game("game_htmls/202012220BRK.html")

# for x in team_a_tables:
#   b = x.find_all("td")
#   for y in b:
#       y.string

