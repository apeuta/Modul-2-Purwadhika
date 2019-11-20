'''
Memasukkan fungsi ke dalam MS Excel
'''
import xlsxwriter
file = xlsxwriter.Workbook("a.xlsx")
sheet = file.add_worksheet("Data")
sheet.write(0, 0, 1)
sheet.write(0, 1, "=A1 + 200")
sheet.write(0, 2, "=SUM(A1:B1)")
for i in range(2,11):
    sheet.write(i-1, 0, i)
file.close()

import xlrd
filerd = xlrd.open_workbook("a.xlsx")
sheetrd = filerd.sheet_by_name("Data")
for i in range(sheetrd.nrows):
    print(sheetrd.cell_value(i, 0))