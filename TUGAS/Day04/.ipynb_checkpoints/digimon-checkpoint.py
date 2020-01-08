import requests
from bs4 import BeautifulSoup
url = "http://digidb.io/digimon-list/"
web = requests.get(url)
data = BeautifulSoup(web.content, "html.parser")
png = []; digi = []; stage = []; pool = []; pool2 = []; jenis = []
att = []; memo = []; equ = []; hp = []; sp = []; atk = []; dfc = []; intl = []; spd = []; gabung = []
num = list (range(1,342))
for i in data.find_all('td', width="21%"):
    png.append(i.get('src'))
for i in data.find_all("a", style="font-weight: bold;"):
    digi.append(i.text)
for i in data.find_all("td", width="9%"):
    stage.append(i.text)
#Creating Pool for Type, Attribute, Memory
for i in data.find_all("td", width="7%"):
    pool.append(i.text)
for i in range (0, len(pool),3):
    jenis.append(pool[i])
for i in range (1, len(pool),3):
    att.append(pool[i])
for i in range (2, len(pool),3):
    memo.append(pool[i])
for i in data.find_all("td", width="8%"):
    equ.append(i.text)
#Creating Pool for HP, SP, ATK, DEF, INT, SPD
for i in data.find_all("td", width=""):
    pool2.append(i.text)
for i in range (0, len(pool2),6):
    hp.append(pool2[i])
for i in range (1, len(pool2),6):
    sp.append(pool2[i])
for i in range (2, len(pool2),6):
    atk.append(pool2[i])
for i in range (3, len(pool2),6):
    dfc.append(pool2[i])
for i in range (4, len(pool2),6):
    intl.append(pool2[i])
for i in range (5, len(pool2),6):
    spd.append(pool2[i])
bagan = list(zip(num, png, digi, stage, att, memo, equ, hp, sp, atk, dfc, intl, spd))
header = [
    "#", "pic", "Digimon", "Stage", "Attribute",
    "Memory", "Equip Slots", "HP", "SP", "ATK", "DEF", "INT", "SPD"
]
for i in range (len(bagan)):
    X = dict(zip(header, bagan[i]))
    gabung.append(X)
import csv
with open("digimon.csv","w",newline="") as x:
    a = csv.DictWriter(x, fieldnames=header)
    a.writeheader()
    a.writerows(gabung)