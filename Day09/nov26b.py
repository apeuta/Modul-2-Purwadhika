import pymongo
import datetime
import pytz
dburl = "mongodb://localhost:27017"
mymongo = pymongo.MongoClient(dburl)
mydb = mymongo["bikinbaru"]
mycol = mydb["cobaaja"]
# mycol.insert_one(
#     {"nama": "Deni", "waktu": datetime.datetime.utcnow()}
# )
# mycol.insert_many([
#     {"nama": "Baim", "waktu": datetime.datetime.now()},
#     {"nama": "Coki", "waktu": datetime.datetime.now()}
# ])
jkt = pytz.timezone("Asia/Jakarta")
query = mycol.find({"nama": "Deni"}, {"waktu":1})
time = (list(query)[0]["waktu"])
print (time)
print (jkt.localize(time))