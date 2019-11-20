'''
Web Scrapping from html file
Install dulu Beautiful Soup
python3 -m pip install beautifulsoup4
'''
from bs4 import BeautifulSoup
data = BeautifulSoup(
    open("coba.html", "r"), "html.parser"
    )
# #prettify untuk menampilkan indentasi
# print (data.prettify())
# print (data.h1)
# #untuk memanggil text dalam tag tertentu
# print (data.h1.text)
# print (data.h1.string)
# #untuk memanggil tag
# print (data.h1.name)
# print (data.ul.text)
# print (data.ul.string)

# #mencari semua tag > menjadikan dalam bentuk list
# print (data.find_all("li"))
# ul = data.ul
# for i in ul.find_all("li"):
#     print (i.text)
# for x in data.find_all("li"):
#     print (x.text)

#Mencari berdasarkan Class
print (data.find_all("li", class_ = "orang"))
ul = data.ul
for i in ul.find_all("li", class_ = "orang"):
    print (i.text)