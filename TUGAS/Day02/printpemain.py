'''
1. get API sportdb, daftar pemain dari sebuah klub
2. input : klub apa? -> X
3. daftar pemain : nama, posisi, usia, negara
save as x. xls & json & csv
'''
import requests
import json
import xlsxwriter
import csv
#Source
klub = input("Ketik nama klub : ")
url = f"https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}"
data = requests.get(url)
players = data.json()["player"]
header = ["nama", "posisi", "usia", "negara"]
nama = []
posisi = []
usia = []
negara = []
hasilAkhir = []
for player in players:
    nama.append(player["strPlayer"])
    posisi.append(player["strPosition"])
    usia.append(2019 - (int(player["dateBorn"][:4])))
    negara.append(player["strNationality"])
kombi = list(zip(nama, posisi, usia, negara))
for i in range(len(kombi)):
    X = dict(zip(header, kombi[i]))
    hasilAkhir.append(X)

#create csv
with open(f'{klub}.csv',"w",newline="") as x:
    kolom = header
    a = csv.DictWriter(x, fieldnames=kolom, delimiter=",")
    a.writeheader()
    a.writerows(hasilAkhir)

#create json
with open (f'{klub}.json', "w") as y:
    json.dump(hasilAkhir,y)

#create excel
newfile = xlsxwriter.Workbook(f"{klub}.xlsx")
newsheet = newfile.add_worksheet("Data Pemain")
for i in range(len(header)):
    newsheet.write(0, i, header[i])
for i in range(len(kombi)):
    for j in range(len(header)):
        newsheet.write(i+1, j, kombi[i][j])
newfile.close()