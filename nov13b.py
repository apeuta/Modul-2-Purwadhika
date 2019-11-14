'''
package
xlswt -> Excel lama
xlsxwriter -> Excel baru
'''
import xlrd
file = xlrd.open_workbook("file.xlsx")
sheet = file.sheet_by_name("Data Karyawan")
data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))
print (data)
import xlsxwriter
newfile = xlsxwriter.Workbook("test123.xlsx")
newsheet = newfile.add_worksheet("Data Karyawan")
'''
sheet.write (row, col, data)
'''
# sheet.write(0, 0, "Nama")
# sheet.write(0, 1, "Kota")
# sheet.write(0, 2, "Job")
for i in range(len(data)):
    for j in range (len(data[0])):
        newsheet.write(i, j, data[i][j])
newfile.close()