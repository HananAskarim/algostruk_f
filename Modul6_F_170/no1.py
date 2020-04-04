#Nomor 1
class Mahasiswa(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

c0 = Mahasiswa('Yoga', 170, 'Sukoharjo', 240000)
c1 = Mahasiswa('Dimas', 151, 'Sragen', 230000)
c2 = Mahasiswa('Rizki', 112, 'Surakarta', 250000)
c3 = Mahasiswa('Aldy', 181, 'Surakarta', 235000)
c4 = Mahasiswa('Fatwa', 154, 'Boyolali', 240000)
c5 = Mahasiswa('Alip', 131, 'Salatiga', 250000)
c6 = Mahasiswa('Irvan', 113, 'Klaten', 245000)
c7 = Mahasiswa('Iqbal', 115, 'Wonogiri', 245000)
c8 = Mahasiswa('Bagus', 123, 'Klaten', 245000)
c9 = Mahasiswa('Azka', 164, 'Karanganyar', 270000)
c10 = Mahasiswa('Bintang', 129, 'Purwodadi', 230000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def urutkanNIM(a):
    baru = {}
    for i in range(len(a)):
        baru[a[i].nama] = a[i].NIM
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elem in listofTuples:
        print (elem[0], ':', elem[1])

urutkanNIM(Daftar)
