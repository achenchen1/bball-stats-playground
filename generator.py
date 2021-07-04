import multiprocessing as mp
import subprocess
import csv

processes_array = []

def runner(game):
    print("done")

def process_creator(url_location, children=4):
    # Load all our urls into a list
    with open("schedule_scraper/urls.txt") as url_file:
        urls = url_file.read().split()

    # Split this list into evenly sized chunks for allocating to pools
    url_arrays = [[] for x in range(0, children)]
    for index in range(children):
        url_arrays[index] = urls[int(len(urls)/children*index):int(len(urls)/children*(index+1))]
    
    m = mp.Manager()
    with mp.Pool(processes=children) as pool:
        for index in range(children):
            processes_array.append(pool.apply_async(runner, args=(urls_array[index])))

        for process:
            processes_array.get()

if __name__ == '__main__':
    process_create(sys.argv[1], sys.argv[2])
