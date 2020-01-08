import requests
host = "https://developers.zomato.com/api/v2.1"
kategori = "/categories"
inputCity = input("Masukkan kota : ")
city = f"/cities?q={inputCity}"
apikey = "6a3792f3d2ab39afa6fbe5b442af12e9"
headInfo = {
    "user-key":apikey
}
urlCity = host + city
kota = requests.get(urlCity, headers=headInfo)
kodeKota = (kota.json()["location_suggestions"][0]["id"])
inputMenu = input("Makanan apa yang ingin anda cari : ")
urlMenu = host + f"/search?entity_id={kodeKota}&entity_type=city&q={inputMenu}"
data = requests.get(urlMenu, headers=headInfo)
data = (data.json()["restaurants"])
for i in range (len(data)):
    ambil = data[i]["restaurant"]
    print (f"+ {ambil['name']}, {ambil['location']['address']}, rating : {ambil['user_rating']['aggregate_rating']}")