'''
Kabisat
'''
tahun = int(input("Input Tahun : "))
def kabisat(x):
    if x % 4 == False:
        print (f"{x} adalah tahun Kabisat")
    else:
        print (f"{x} bukanlah tahun Kabisat")
kabisat(tahun)