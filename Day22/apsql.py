from flask import Flask, jsonify, request, render_template, redirect
import mysql.connector as mc
app = Flask(__name__)

'''
KILL PORT
sudo lsof -i:{port}
kill {PID}
'''

dbku = mc.connect(
    host="localhost",
    user= "root",
    passwd= "12345",
    database= "testing"
)

#Create form interface
@app.route("/")
def home():
    return render_template("form.html")

#post data with html
@app.route("/form", methods= ["POST"])
def formulir():
    if request.method == "POST":
        body = request.form
        x = dbku.cursor()
        data = (body["nama"], body["usia"])
        sql = f"insert into datadiri (nama, usia) values {data}"
        x.execute(sql)
        dbku.commit()
        return redirect("/data")

#connect with sql database
@app.route("/data", methods= ["GET", "POST"])
def data():
    if request.method == "GET":
        x = dbku.cursor()
        x.execute("select * from datadiri")
        hasil = x.fetchall()
        hasil = list (map(lambda i: {
            "id":i[0], "nama":i[1], "usia":i[2]
        }, hasil))
        return jsonify(hasil)
    elif request.method == "POST":
        body = request.json
        x = dbku.cursor()
        data = (body["nama"], body["usia"])
        sql = f"insert into datadiri (nama, usia) values {data}"
        x.execute(sql)
        dbku.commit()
        return "DATA POSTED!"

@app.route("/data/<int:no>", methods= ["GET"])
def datano(no):
    x = dbku.cursor()
    sql = f"select * from datadiri where id = {no}"
    x.execute(sql)
    hasil = x.fetchall()
    hasil = list (map(lambda i: {
        "id":i[0], "nama":i[1], "usia":i[2]
    }, hasil))
    return jsonify(hasil)

if __name__ == "__main__":
    app.run(debug=True)