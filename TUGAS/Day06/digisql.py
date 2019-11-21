import csv
with open ("digimon.csv", "r") as x:
    baca = csv.DictReader(x)
    digi = (list(baca))
data = []
for i in digi:
    data.append(tuple(i.values()))
print (data[0])
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "Apeuta42",
    database = "cobaaja"
)
c = db.cursor()
# sql1 = "describe digi"
# c.execute(sql1)
# print (c.fetchall())
sql2 = "insert into digi (no, pic, digimon, stage, attr, memo, equip, hp, sp, atk, def, intl, spd) values (%s, %s, %s, %s,%s, %s,%s, %s, %s, %s,%s, %s)"
val = data[0]
c.execute(sql2, val)
db.commit()
print (c.rowcount, "Data Tersimpan")