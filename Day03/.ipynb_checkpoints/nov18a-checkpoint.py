'''
Money Value Converter
'''
import requests
bank = input("Masukkan nama bank : ")
url = f"https://kurs.web.id/api/v1/{bank.lower()}"
data = requests.get(url).json()
buy = int(data["beli"])
sell = int(data ["jual"])
X = int(input("Kode tukar \n (1) USD -> IDR\n (2) IDR -> USD\n (3) USD -> Bitcoin \n (4) IDR -> Bitcoin \nMasukkan kode : "))
if X == 2 :
    Y = int(input("Masukkan nominal yang akan ditukar : Rp "))
    print (f"Harga jual dari bank {bank.upper()} saat ini adalah {sell}")
    print (f"IDR {Y} = USD {round(Y/sell),2}")
elif X == 1:
    Y = int(input("Masukkan nominal yang akan ditukar : US$ "))
    print (f"Harga beli dari bank {bank.upper()} saat ini adalah {buy}")
    print (f"USD {Y} = IDR {Y*buy}")
elif X == 3:
    url = "https://blockchain.info/ticker"
    data = requests.get(url).json()["USD"]["buy"]
    Y = int(input("Masukkan nominal yang akan ditukar : US$ "))
    rasio = 1/data
    print (f"USD {Y} = {round((Y*rasio),2)} BTC")
elif X == 4:
    url = "https://blockchain.info/ticker"
    data = requests.get(url).json()["USD"]["buy"]
    Y = int(input("Masukkan nominal yang akan ditukar : IDR "))
    Z = Y/sell
    rasio = (1/data)
    print (f"IDR {Y} = {round((Z*rasio),2)} BTC")