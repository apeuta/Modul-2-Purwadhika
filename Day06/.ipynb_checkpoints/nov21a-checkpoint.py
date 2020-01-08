import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "12345",
    database = "ptABC"
)
c = db.cursor()
c.execute("create table owner (no int, nama varchar(50))")
# sql1 = "insert into karyawan (nama, gaji) values (%s, %s)"
# val = ("Andi", 20000000)
# c.execute (sql1, val)
# db.commit()
# print (c.rowcount, "Data Tersimpan")
# sql2 = "insert into karyawan (nama, gaji) values (%s, %s)"
# val2 = [("Aye", 20000000),( "Fyuwi", 3200000)]
# c.executemany (sql2, val2)
# db.commit()
# print (c.rowcount, "Data Tersimpan")