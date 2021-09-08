# Fetches all the 2021 games

from bs4 import BeautifulSoup
from io import BytesIO
import pycurl

# Get our instances running
cURL = pycurl.Curl()
e = BytesIO()
cURL.setopt(cURL.WRITEDATA, e)

# Pull html for each of these webpages
months_list = ["december", "january", "february", "march", "april", "may", "june", "july"]
for month in months_list:
    cURL.setopt(cURL.URL, 'https://www.basketball-reference.com/leagues/NBA_2021_games-{}.html'.format(month))
    cURL.perform()

    with open("{}.html".format(month), "wb+") as output_file:
        output_file.write(e.getbuffer())

    e.flush()

