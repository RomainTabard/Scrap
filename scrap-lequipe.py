import bs4
import re
import urllib.request
from urllib.request import Request, urlopen
 
#Url utilisée pour le scraping
url="https://www.lequipe.fr/Football/match/406316"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
soup = bs4.BeautifulSoup(webpage, 'html.parser')
#fichier = open("MPGStats.txt", "w")

#t = soup.find(class_='index__root___1KIse')
#titre = t.h4.get_text()


#fichier.write(titre)
f#ichier.close()