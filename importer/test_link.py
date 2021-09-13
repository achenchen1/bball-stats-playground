from single_game import single_game
from os import path, listdir
import queue
import sqlite3
import threading
import time

processes_array = []

def inserter_function(data_lock, connection, db_lock, data_queue):
    while True:
        with data_lock:
            if data_queue.empty():
                return
            queue_item = data_queue.get()
            game_id = queue_item[1]
            game_html = path.join("game_htmls", queue_item[0])

        game = single_game(game_html)

        with db_lock:
            for team in game:
                for player in team.players:
                    stats = game[team][player]["stats"]
                    name = game[team][player]["name"]

                    for box_score in stats:
                        # For now, we only want "actual" quarters and OTs; no halves, and no advanced stats
                        if box_score.quarter[0] == "Q" or box_score.quarter[0] == "O":
                            if "DNP" not in box_score.stats:
                                connection.execute("""
                                INSERT INTO  test_table
                                (game_id, player_id, team, mp, fg, fga, fg_pct, fg3, fg3a, fg3_pct, ft, fta, ft_pct, orb, drb, trb, ast, stl, blk, tov, pf, pts, plus_minus)
                                VALUES
                                ('{game_id}', '{player_id}', '{team}', '{mp}', '{fg}', '{fga}', '{fg_pct}', '{fg3}', '{fg3a}', '{fg3_pct}', '{ft}', '{fta}', '{ft_pct}', '{orb}', '{drb}', '{trb}', '{ast}', '{stl}', '{blk}', '{tov}', '{pf}', '{pts}', '{plus_minus}');""".format(**{"game_id": game_id, "player_id": player, "team": team.abbreviation, **box_score.stats}));
                            # If they DNP, then just auto-populate with NULL
                            else:
                                connection.execute("""
                                INSERT INTO  test_table
                                (game_id, player_id, team)
                                VALUES
                                ('{game_id}', '{player_id}', '{team}');""".format(**{"game_id": game_id, "player_id": player, "team": team.abbreviation}));
            connection.commit()

def thread_creator(children=4):
    connection = sqlite3.connect('2021.db', check_same_thread=False)

    threads = []
    thread_lock = threading.Lock()
    db_lock = threading.Lock()
    data_queue= queue.Queue()

    htmls = listdir("game_htmls")
    for i, val in enumerate(htmls):
        data_queue.put((val, i))

    for _ in range(children):
        threads.append(threading.Thread(target=inserter_function, args=(thread_lock, connection, db_lock, data_queue)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    connection.close()

thread_creator(8)
