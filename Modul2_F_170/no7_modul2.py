import no2_modul2

class MhsTIF(no2_modul2.Mahasiswa):     # class induknya : Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Python is cool')

#Metode atau state yang muncul berasal dari semua class Manusia, Mahasiswa,
#MhsTIF. Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, dan itu
#membuat MhsTIF mewarisi semua properties dari Mahasiswa dan Manusia.

#ambilNama merupakan metode yg berasal dari class Mahasiswa
#ambilNIM merupakan metode yg berasal dari class Mahasiswa
#ambilUangS merupakan metode yg berasal dari class Mahasiswa
#makan merupakan metode yg berasal dari class Mahasiswa
#keadaan merupakan state yg berasal dari class Mahasiswa
#NIM merupakan state yg berasal dari class Mahasiswa
#nama merupakan state yg berasal dari class Mahasiswa
#kota merupakan state yg berasal dari class Mahasiswa
#katakanPy merupakan metode yg berasal dari class MhsTIF
#mengalikanDenganDua merupakan metode yg berasal dari class Manusia
        
        
