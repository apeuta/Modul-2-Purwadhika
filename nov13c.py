'''
json => xlsx
'''
# import json
# with open ("file.json", "r") as x:
#     baru = json.load(x)
# A = list(baru[0].keys())
# B = []
# for i in range(len(baru)):
#     B.append(list(baru[i].values()))
# import xlsxwriter
# newfile = xlsxwriter.Workbook("coba.xlsx")
# newsheet = newfile.add_worksheet("Data Karyawan")
# for i in range(len(A)):
#     newsheet.write(0, i, A[i])
# for i in range(len(B)):
#     for j in range(len(A)):
#         newsheet.write(i+1, j, B[i][j])
# newfile.close()
'''
csv => xlsx
'''
import csv
with open ("file.csv", "r") as x:
    baca = csv.DictReader(x)
    C = (list(baca))
A = list(C[0].keys())
B = []
for i in C:
    B.append(list(i.values()))
import xlsxwriter
newfile = xlsxwriter.Workbook("cobalagi.xlsx")
newsheet = newfile.add_worksheet("Data Karyawan")
for i in range(len(A)):
    newsheet.write(0, i, A[i])
for i in range(len(B)):
    for j in range(len(A)):
        newsheet.write(i+1, j, B[i][j])
newfile.close()