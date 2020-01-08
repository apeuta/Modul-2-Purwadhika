import pandas as pd
import mysql.connector
import sqlalchemy as salc
# import pymysql
# pymysql.install_as_MySQLdb()

query = "select * from employees"
engine = salc.create_engine("mysql://root:12345@localhost:3306/pandas_tes")
df = pd.read_sql("query", engine)
print (df)