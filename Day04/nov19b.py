import requests
from bs4 import BeautifulSoup
web = requests.get("http://127.0.0.1:5500/Coding/DATAVIZ/Day%204/coba.html")
data = BeautifulSoup(web.content, "html.parser")
ul = data.ul
for i in ul.find_all("li", class_= "orang"):
    print (i.text)