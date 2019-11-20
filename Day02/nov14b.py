'''
Python get API
requests
if you can't import it, need to install it first
'''
import requests
# url = "https://jsonplaceholder.typicode.com/users"
# data = requests.get(url)
# print (data.json())
# print (type(data.json()))
# print (data.json()["name"])
# print (data.json()["address"]["street"])
# for i in data.json():
#     print (i["name"], "tinggal di", i["address"]["street"])

'''
Import nama pemain
'''
# klub = input("Ketik nama klub : ")
# url2 = f"https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}"
# data = requests.get(url2)
# players = data.json()["player"]
# for player in players:
#     print (f'{player["strPlayer"]} ({player["strPosition"]})')
'''
Import weather
'''
# x = "&appid=287dbd23fabfc16966a10fdba6960088"
# y = input("Ketik kota : ")
# url = f"http://api.openweathermap.org/data/2.5/weather?q={y}{x}"
# data = requests.get(url)
# cuaca = data.json()
# sunrise = cuaca["sys"]["sunrise"]
# sunset = cuaca["sys"]["sunset"]
# suhu = cuaca["main"]["temp"]
# print (f"{suhu - 273}'C ")
# from datetime import datetime
# from dateutil import tz
# myzone = tz.gettz("Asia/Jakarta")
# waktu = datetime.utcfromtimestamp(int(sunrise))
# print (waktu)