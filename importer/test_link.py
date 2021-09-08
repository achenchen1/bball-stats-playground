from single_game import single_game
from os import path, listdir
import sqlite3
import threading

processes_array = []

def inserter_function(data_lock, connection, db_lock, html_queue, game_id):
    with data_lock:
        game_id += 1
        game_html = path.join("game_htmls", html_queue.get())

    game = single_game(game_html)

    with db_lock:
        for team in game:
            players = team.players
            for player in players:
                stats = player["stats"]
                name = player["name"]


    




for a in x:
    print(a.name)
    print(a.abbreviation)
    print(a.players)

# print(x)
