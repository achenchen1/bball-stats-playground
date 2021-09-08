import sqlite3
import threading

processes_array = []

def tester(i, lock, test):
    for x in range(999):
        with lock:
            rc = test.execute("INSERT INTO  \"test_table\" (\"game_id\", \"player_id\", \"mp\", \"fg\", \"fga\", \"fg_pct\", \"fg3\", \"fg3a\", \"fg3_pct\", \"ft\", \"fta\", \"ft_pct\", \"orb\", \"drb\", \"trb\", \"ast\", \"stl\", \"blk\", \"tov\", \"pf\", \"pts\", \"plus_minus\") VALUES ('{0}', '{0}', '{0}', '{0}', '{0}', '{0}.0', '{0}', '{0}', '{0}.0', '{0}', '{0}', '{0}.0', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}.0');".format(x%7+i*10));
            if x%7 == 6:
                test.commit()

    #print(threading.current_thread())
    #print(threading.main_thread())
    #print("test val {}".format(test))

def process_creator(children=4):
    test = sqlite3.connect('2021.db', check_same_thread=False)
    threads = []
    thread_lock = threading.Lock()
    for i in range(9):
        threads.append(threading.Thread(target=tester, args=(i, thread_lock, test)))
   
    for t in threads:
        t.start()

    print(threading.active_count())
    print(threading.current_thread())

    for t in threads:
        t.join()

    test.close()


if __name__ == '__main__':
    process_creator()

