from bs4 import BeautifulSoup
from stat_structures import Team, BoxScore

def single_game(file_name):
    """
    Extracts stats from a single game from the cURL'd HTML file

    :param file_name: file path of HTML file extracted from basketball reference
    :return: dict indexable by Teams, with the values identical to return from players_stats_from_tables
    """
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

    team_a_stats = players_stats_from_tables(team_a_tables)
    team_b_stats = players_stats_from_tables(team_b_tables)
    
    team_a.players.extend(team_a_stats.keys())
    team_b.players.extend(team_b_stats.keys())

    return {team_a: team_a_stats, team_b: team_b_stats}



def players_stats_from_tables(team_tables):
    """
    Generates the stats for all the players of a particular team.
    Note as of Sept 7th, the advanced stats and stats for a half are unused (and parsed out) by the SQL importer; the ability to extract them have been left in.

    :param team_tables: tables containing stats for a team
    :return: dict of players indexable by player name_id, which has a value that is a dict, which is indexable by string "stats" for a list of stats for each quarter/half/overtime/advanced-stats, and "name" for full name.
    """
    # Don't have a collection of the players yet. We assume that the full box score has all the players
    players = {}
    for row in team_tables[0]:
        players[get_name_id_from_row(row)] = {"stats": [], "name": row.find("th").string}

    # Want to omit the last one, since that one is "advanced stats"
    for table_num, table in enumerate(team_tables[:-1]):
        if table_num == 0:
            quarter = "Box Score"
        elif table_num == 3 or table_num == 6:
            quarter = "H{}".format(table_num // 3)
        elif table_num > 6:
            quarter = "OT{}".format(table_num - 6)
        else:
            quarter = "Q{}".format(table_num - table_num//3)

        for row in table:
            box_score = BoxScore(row.find_all("td"), quarter)
            name_id = get_name_id_from_row(row)
            players[name_id]["stats"].append(box_score)

    # Parse last table
    for row in team_tables[-1]:
        quarter = "ADV"
        box_score = BoxScore(row.find_all("td"), quarter)
        name_id = get_name_id_from_row(row)
        players[name_id]["stats"].append(box_score)

    return players
        
def get_name_id_from_row(row):
    tag = row.find("th")
    if "data-append-csv" in tag.attrs:
        return tag["data-append-csv"]

    player_url = tag.find("a")["href"]
    return player_url[player_url.rfind("/")+1:-5]
