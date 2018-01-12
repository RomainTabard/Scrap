import bs4
import re
import urllib.request
from urllib.request import Request, urlopen
 
#Url utilisée pour le scraping
url="http://www.meteofrance.com/previsions-meteo-france/nantes/44000"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
soup = bs4.BeautifulSoup(webpage, 'html.parser')
fichier = open("Meteo.txt", "w")

t=soup.find(id=re.compile('town-forecast'))
ville = t.h1.get_text()
fichier.write(ville)
fichier.write('\n')
date0 = t.find(class_='liste-jours').find_all(class_='active')
date = date0[0].a.get_text()
mintemp = date0[0].find(class_='min-temp').get_text()
maxtemp = date0[0].find(class_='max-temp').get_text()
fichier.write(date + '\n'+ mintemp + '\n'+ maxtemp + '\n')

liste = t.find(class_='liste-jours').find('ul')
demain = liste.find_all('li')
demain1 = demain[1].a.get_text()
fichier.write(demain1+'\n')
fichier.write('\n')
fichier.close()