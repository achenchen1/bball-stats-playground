import sqlite3
import threading

processes_array = []

def tester(i):
    test = sqlite3.connect('2021.db', check_same_thread=False)
    rc = test.execute("INSERT INTO  \"test_table\" (\"game_id\", \"player_id\", \"mp\", \"fg\", \"fga\", \"fg_pct\", \"fg3\", \"fg3a\", \"fg3_pct\", \"ft\", \"fta\", \"ft_pct\", \"orb\", \"drb\", \"trb\", \"ast\", \"stl\", \"blk\", \"tov\", \"pf\", \"pts\", \"plus_minus\") VALUES ('{0}', '{0}', '{0}', '{0}', '{0}', '{0}.0', '{0}', '{0}', '{0}.0', '{0}', '{0}', '{0}.0', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}.0');".format(i));
    i += 1
    test.commit()
    test.close()
    #print(threading.current_thread())
    #print(threading.main_thread())
    #print("test val {}".format(test))

def process_creator(children=4):
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=tester, args=(i,)))
   
    for t in threads:
        t.start()

    print(threading.active_count())
    print(threading.current_thread())

    for t in threads:
        t.join()


if __name__ == '__main__':
    process_creator()

