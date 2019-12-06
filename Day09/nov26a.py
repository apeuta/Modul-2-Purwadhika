import pymongo
dburl = "mongodb://localhost:27017"
mymongo = pymongo.MongoClient(dburl)
# #Cek database apa yang ada di mongo
# dbs = mymongo.list_database_names()
# print (dbs)

#Cek data dalam collection
mydb = mymongo["pymongodb"]
mycol = mydb["colmong"]
alldata = list(mycol.find())
# print (alldata)
# cariAndi = list(mycol.find({"nama":"Andi"}, {"nama":1, "_id":0}))
# print (cariAndi)
# cariUsia = list(mycol.find({"usia": {"$gt":24}}))
# print (cariUsia)

# #Inputing Data
# mydata = {
#     "nama": "Deni",
#     "usia": 18,
#     "kota": "Kediri"
# }
# mycol.insert_one(mydata)
# dataBanyak = [
#     {"nama": "Euis", "usia": 35, "kota": "Denpasar"},
#     {"nama": "Fafa", "usia": 29, "kota": "Jakarta"},
#     {"nama": "Gian", "usia": 22, "kota": "Sorong"}
# ]

# #Melihat objek ID data yang diinput
# x = mycol.insert_many(dataBanyak)
# print (x.inserted_ids)
# #Mencari banyak data
# nama = ["Andi", "Euis", "Fafa"]
# print(list(mycol.find({"nama": {"$in": nama}})))

# #Delete data
# y = {"nama": "Gian"}
# mycol.delete_one(y)

#Update Data
# lama = {"nama": "Euis"}
# baru = {"nama": "Eka"}
# mycol.update_one(lama, {"$set": baru})
old = {
    "$and":[
        {"usia": {"$gt": 25}},
        {"usia": {"$lt": 30}}
    ]
}
baru2 = {"nama": "Young Man"}
mycol.update_many(old, {"$set": baru2})