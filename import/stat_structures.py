class Team:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.players = []

class BoxScore:
    def __init__(self, stats_list):
        self.stats = {}
        # if there's a "reason", it means they didn't play.
        if stats_list[0]["data-stat"] == "reason":
            self.stats["DNP"] = None
        else:
            for stat in stats_list:
                if "poptip" in stat["class"]:
                    data_tip = stat["data-tip"]
                    # First three are obpm, dbpm, vorp
                    separated = data_tip.split("<br>")[:-1]
                    for s in separated:
                        s = s.strip().lower()
                        self.stats[s[:s.find(":")]] = float(s[s.find(" ")+1:])

                if stat["data-stat"] != "mp":
                    self.stats[stat["data-stat"]] = float(0 if stat.string is None else stat.string)
                else:
                    self.stats[stat["data-stat"]] = stat.string

