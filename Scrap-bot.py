import bs4
import re
import urllib.request
from urllib.request import Request, urlopen
 
#Url utilisée pour le scraping
url="http://www.mpgstats.fr/top/Premier-League/season"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
soup = bs4.BeautifulSoup(webpage, 'html.parser')
fichier = open("MPGStats.txt", "w")

for t in soup.find_all(id=re.compile('^tableau_.*'), limit =4):
    categorie = t.h4.span.get_text('', strip=True)
    fichier.write(categorie+ '\n')
    #for player in t.find_all('tr', class_='player success ', limit = 5):
    for player in t.find_all(itemprop='member', limit = 5):    
    #for player in t.find_all(id='joueur', limit =5):
        name = player.find(id='joueur').get_text(' ', strip=True)
        club = player.find(itemprop='homeLocation').get_text(' ',strip=True)
        #year = d.find(class_='year_column').get_text(' ', strip=True)
        #name = d.b.get_text(' ', strip=True)    
        fichier.write(name+" - "+ club+'\n')
    fichier.write('\n')
fichier.close()