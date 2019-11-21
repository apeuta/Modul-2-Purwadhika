import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "Apeuta42",
    # database = "ptABC"
)
c = db.cursor()
# c.execute("select * from karyawan")
# print (c.fetchall())
sql = "insert into karyawan (nama, gaji) values (%s, %s)"
val = ("Andi", 20000000)
c.execute (sql, val)
db.commit()
print (c.rowcount, "Data Tersimpan")
