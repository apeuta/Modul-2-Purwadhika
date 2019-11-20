import xlrd
'''
How to install
pip install xlrd
python3 -m pip install xlrd
conda install xlrd
'''
file = xlrd.open_workbook("file.xlsx")
# sheet = file.sheet_by_index(0)
sheet = file.sheet_by_name("Data Karyawan")
# print (sheet.nrows, sheet.ncols)
'''
Value
row (1,2,...),col(A,B,...)
'''
# print (sheet.cell_value(0,0))
# print (sheet.cell_value(1,0))
# print (sheet.cell_value(0,1))
'''
Cek nama kolom di excel
'''
# #Cara 1
# cols = []
# for i in range(sheet.ncols):
#     cols.append(sheet.cell_value(0,i))
# print (cols)

# #Cara 2
# print (sheet.row_values(0))
'''
Cara dapat semua data
'''
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))
'''
xlsx => json
'''
A = sheet.row_values(0)
print (A)
B = []
for i in range(1,(sheet.nrows)):
    B.append(sheet.row_values(i))
print (B)
C = []
for j in range(len(B)):
    a = dict(zip(A,(B[j])))
    C.append(a)
print (C)
import json
with open ("file.json", "w") as y:
    json.dump(C,y)
'''
xlsx => csv
'''
import csv
with open("file.csv","w",newline="") as x:
    kolom = A
    a = csv.DictWriter(x, fieldnames=kolom, delimiter=",")
    a.writeheader()
    a.writerows(C)