import pycurl
from io import BytesIO 

crl = pycurl.Curl() 
e = BytesIO()
crl.setopt(crl.URL, 'https://www.basketball-reference.com/leagues/NBA_2021_games-december.html')
# crl.setopt(crl.URL, 'https://wiki.python.org/moin/BeginnersGuide')


crl.setopt(crl.WRITEDATA, e)

crl.perform() 
crl.close()

with open("output_1.txt", "wb+") as f:
    f.write(e.getbuffer())
