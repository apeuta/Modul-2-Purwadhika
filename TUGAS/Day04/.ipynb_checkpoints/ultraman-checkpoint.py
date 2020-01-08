import requests
from bs4 import BeautifulSoup
web = requests.get("http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/")
data = BeautifulSoup(web.content, "html.parser")
out = []
for i in data.find_all("strong"):
    out.append(i.text)
ultra = out [2:36]
monster = out [37:110]
# print (ultra)
# print (monster)
for i in ultra:
    print (i)
for j in monster:
    print(j)