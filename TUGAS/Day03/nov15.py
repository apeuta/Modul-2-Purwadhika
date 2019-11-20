import xlsxwriter
file = xlsxwriter.Workbook("Challenge.xlsx")
sheet1 = file.add_worksheet("sheet 1")
sheet2 = file.add_worksheet("sheet 2")
sheet3 = file.add_worksheet("sheet 3")
sheet4 = file.add_worksheet("sheet 4")

n=1
for i in range (3):
    for j in range (3):
        sheet1.write(i, j, n)
        n +=1
    n -= 2

n=3
for i in range (3):
    for j in range (3):
        sheet2.write(i, j, n)
        n +=3
    n -= 10

n=3
for i in range (3):
    for j in range (3):
        sheet3.write(i, j, n)
        n -=1
    n += 6

n=9
for i in range (3):
    for j in range (3):
        sheet4.write(i, j, n)
        n -= 3
    n += 8

file.close()