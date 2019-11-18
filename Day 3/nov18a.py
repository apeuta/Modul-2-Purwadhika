import requests
import json
bank = input("Masukkan nama bank : ")
url = f"https://kurs.web.id/api/v1/{bank.lower()}"
data = requests.get(url).json()
X = int(input("Mau tukar ke rupiah (1) atau ke dolar (2) : "))
Y = int(input("Masukkan nominal yang akan ditukar : "))
if X == 2 :
    print (f"Harga beli dari bank {bank.upper()} saat ini adalah {data['beli']}")
    print (f"IDR {Y} = USD {Y/(int(data['beli']))}")
else:
    print (f"Harga beli dari bank {bank.upper()} saat ini adalah {data['jual']}")
    print (f"USD {Y} = IDR {Y*(int(data['jual']))}")