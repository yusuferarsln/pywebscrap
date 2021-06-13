import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

companylinks = []
for i in range(1,18):

    kelime = "kapi"
    url = "https://tr.kompass.com/searchCompanies?acClassif=&localizationCode=&localizationLabel=&localizationType=&text="+kelime+"&searchType=SUPPLIER"
    sayfa = urllib.request.urlopen(url)
    soup = BeautifulSoup(sayfa, "html.parser")

    ana = soup.find(id = "result-entreprise")
    alt = ana.find_all('a',class_="addList row rowFlex")
    links = [a.get('href') for a in alt]
    for s in links:
        try:
            inurl = s
            inpage = urllib.request.urlopen(inurl)
            insoup = BeautifulSoup(inpage, "html.parser")

            baba = insoup.find('div',class_="companyWeb")
            final = baba.find('a', class_="ListWww")
            companylinks.append(final.get("href"))
        except:
            print("Başaramadık")
f= open('source.txt','w')
p = 0
for n in companylinks:
    try:
        url = n
        sayfa = urllib.request.urlopen(url)
        soup = BeautifulSoup(sayfa, "html.parser")
        mail = soup.find(string=re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"))
        f.write(mail+"\n")
        print(p)
        p = p+1
    except:
        print("Bulamadım")
        p = p+1

f.close()