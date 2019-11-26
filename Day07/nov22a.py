import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "Apeuta42",
    database = "ptabc"
)
c = db.cursor(dictionary=True)
# query = "select nama from karyawan"
# c.execute(query)
# out = c.fetchall()
# print (out) #get tuple with 2 objects
# print (list(map(lambda x: x[0], out)))
# #menambah data
# query1 = "update karyawan set nama = %s, gaji = %s where no = %s"
# data = ("Zizi", 15000000, 5)
# c.execute(query1, data)
# db.commit()
query2 = "alter table karyawan add column hobby varchar(255)"
c.execute(query2)
db.commit()