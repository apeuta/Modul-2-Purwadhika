import xlrd
import xlsxwriter
excel = input("Masukkan nama file excel : ")
asal = input("Masukkan nama sheet dasar yang akan diupdate datanya : ")
tujuan = input("Masukkan nama sheet baru untuk update : ")
file = xlrd.open_workbook(excel)
sheet = file.sheet_by_name(asal)
data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))

newfile = xlsxwriter.Workbook(excel)
sheet1 = newfile.add_worksheet(asal)
newsheet = newfile.add_worksheet(tujuan)
for i in range(len(data)):
    for j in range (len(data[0])):
        sheet1.write(i, j, data[i][j])
for i in range(len(data)):
    for j in range (len(data[0])):
        newsheet.write(i, j, data[i][j])
def dataBaru():
    noUrut = len(data)
    ask = input("Apakah anda ingin menambahkan data (Y/N) : ")
    while ask == ("Y"):
        A = input("Masukkan nama : ")
        B = input("Masukkan kota : ")
        C = [(noUrut), A, B]
        for j in range (len(data[0])):
            newsheet.write(noUrut,j,C[j])
        noUrut += 1
        ask = input("Apakah anda ingin menambahkan data (Y/N) : ")
        if ask == ("N"):
            break

dataBaru()
newfile.close()