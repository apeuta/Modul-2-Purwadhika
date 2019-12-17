from flask import Flask, jsonify, abort, render_template, send_from_directory
server = Flask(__name__)

#home route
@server.route("/")
def home():
    return "<h1>Halooo!!</h1>"

#render html
@server.route("/html")
def html():
    return render_template("html.html")

#send data and render html
@server.route("/data")
def data():
    nama = "Andi"
    kota = "Jakarta"
    return render_template("data.html", 
            hihi= {"name": nama, "city": kota})

karyawan = [
    {"id": 1, "nama": "Andi", "usia": 20, "kota":"Jakarta"},
    {"id": 2, "nama": "Budi", "usia": 21, "kota":"Jakarta"},
    {"id": 3, "nama": "Caca", "usia": 22, "kota":"Jakarta"},
    {"id": 4, "nama": "Deni", "usia": 23, "kota":"Jakarta"},
    {"id": 5, "nama": "Euis", "usia": 25, "kota":"Jakarta"}
]

#route response json
@server.route("/karyawan")
def jons():
    return jsonify(karyawan)

#error route
@server.errorhandler(404)
def notFound(error):
    return render_template("error.html")

#dynamic route response json
@server.route("/karyawan/<int:id>")
def idkar(id):
    if id > len(karyawan) or id < 1:
        abort(404)
    else:
        return jsonify(karyawan[id-1])

#render static file: storage
@server.route("/file/<path:namaFile>")
def gambar(namaFile):
    return send_from_directory("storage", namaFile)

if __name__ == "__main__":
    server.run(debug= True)