# data = open ("data.txt", "r")
# x = data.read().split(", ")[::-1]
# # print (x)
# for i in x:
#     print (i)

# output = open ("x.txt", "a")
# for i in x:
#     output.write(i + "\n")

'''
Cara 1
'''
# file = open ("file.csv","r")
# x = file.read().split("\n")
# y = []
# for a in x:
#     a = a.split(",")
#     y.append(a)
# listDasar = y[0]
# C = []
# for m in range(len(y)-1):
#     a = dict(zip(lisßtDasar,(y[1:][m])))
#     C.append(a)
# print (C)

'''
Cara 2
'''
# import csv
# with open ("file.csv", "r") as x:
#     baca = csv.reader(x)
#     e = (list(baca))

# header = list(e[0])
# table = list(e[1:])
# C = []
# for m in range(len(table)):
#     a = dict(zip(header,(table[m])))
#     C.append(a)
# print (C)

'''
Cara 3
'''
# import csv
# with open ("file.csv", "r") as x:
#     baca = csv.DictReader(x)
#     print (list(baca))

'''
Menulis csv dari dictionary
'''
# import csv
# data = [
#     {"nama":"Andi", "usia":22, "kota":"Jakarta"},
#     {"nama":"Budi", "usia":23, "kota":"Jakarta"},
#     {"nama":"Caca", "usia":24, "kota":"Jakarta"}
# ]

# with open("cobaBaru.csv","w",newline="") as x:
#     kolom = ["nama", "usia", "kota"]
#     a = csv.DictWriter(x, fieldnames=kolom, delimiter=",")
#     a.writeheader()
#     a.writerows(data)

'''
Import json
'''
# import json

# with open ("trial11.json", "r") as x:
#     out = json.load(x)

# print(out)

# with open ("haha.json", "w") as y:
#     json.dump(out,y)

'''
TRIAL
json to csv
'''
# import json

# with open ("haha.json", "r") as x:
#     out = json.load(x)

# import csv
# with open("haha.csv","w",newline="") as x:
#     kolom = ["nama", "usia"]
#     a = csv.DictWriter(x, fieldnames=kolom, delimiter=",")
#     a.writeheader()
#     a.writerows(out)

'''
TRIAL
csv to json
'''
# import csv
# with open ("cobaBaru.csv", "r") as x:
#     baca = csv.DictReader(x)
#     C = (list(baca))   
# import json
# with open ("cobaBaru.json", "w") as y:
#     json.dump(C,y)