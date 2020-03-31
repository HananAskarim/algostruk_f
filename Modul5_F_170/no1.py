from Latihan import *

class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + '. tiap bulannya.'
        return s

c0 = MhsTif("Yoga", 170, "Sukoharjo", 240000)
c1 = MhsTif("Dimas", 151, "Sragen", 230000)
c2 = MhsTif("Rizki", 112, "Surakarta", 250000)
c3 = MhsTif("Aldy", 181, "Surakarta", 235000)
c4 = MhsTif("Fatwa", 154, "Boyolali", 240000)
c5 = MhsTif("Alip", 131, "Salatiga", 250000)
c6 = MhsTif("Irvan", 113, "Klaten", 245000)
c7 = MhsTif("Iqbal", 115, "Wonogiri", 245000)
c8 = MhsTif("Bagus", 123, "Klaten", 245000)
c9 = MhsTif("Azka", 164, "Karanganyar", 270000)
c10 = MhsTif("Bintang", 129, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def urutkanNim(list):
    NIM = []
    for i in list:
        NIM.append(i.nim)
    insertionSort(NIM)
    return NIM

llist = urutkanNim(Daftar)
print(llist)
