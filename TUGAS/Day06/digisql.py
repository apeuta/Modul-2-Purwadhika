import csv
with open ("digimon.csv", "r") as x:
    baca = csv.DictReader(x)
    digi = (list(baca))
data = []
for i in digi:
    data.append(tuple(i.values()))
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "Apeuta42",
    database = "digimon"
)
c = db.cursor()
# sql1 = "create table digi (no text, pic text, digimon text, stage text, attr text, memo text, equip text, hp text, sp text, atk text, def text, intl text, spd text)"
# c.execute(sql1)
sql2 = "insert into digi (no, pic, digimon, stage, attr, memo, equip, hp, sp, atk, def, intl, spd) values (%s, %s, %s, %s,%s, %s,%s, %s, %s, %s,%s, %s, %s)"
c.executemany(sql2, data)
db.commit()
print (c.rowcount, "Data Tersimpan")