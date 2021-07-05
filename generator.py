from io import BytesIO
import multiprocessing as mp
import pycurl

processes_array = []

def fetcher(games):
    cURL = pycurl.Curl()

    for game_url in games:
        e = BytesIO()
        cURL.setopt(cURL.WRITEDATA, e)
        cURL.setopt(cURL.URL, "https://www.basketball-reference.com{}".format(game_url))
        cURL.perform()

        with open("{}".format(game_url.rsplit('/', 1)[-1]), "wb+") as output_file:
            output_file.write(e.getbuffer())

        del e


def process_creator(children=4):
    # Load all our urls into a list
    with open("schedule_scraper/urls.txt") as url_file:
        urls = url_file.read().split()

    # Split this list into evenly sized chunks for allocating to pools
    url_arrays = [[] for x in range(0, children)]
    for index in range(children):
        url_arrays[index] = [urls[int(len(urls)/children*index):int(len(urls)/children*(index+1))]]
    
    m = mp.Manager()
    with mp.Pool(processes=children) as pool:
        for index in range(children):
            processes_array.append(pool.apply_async(fetcher, args=(url_arrays[index])))

        for process in processes_array:
            process.get()

if __name__ == '__main__':
    process_creator()
