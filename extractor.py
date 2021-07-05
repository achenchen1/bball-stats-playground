from bs4 import BeautifulSoup

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

