from Latihan import *

A = [2,4,6,7,9,11]
B = [1,3,5,8,10,12,13]

def urutkan(array1, array2):
    C = array1 + array2
    selectionSort(C)
    return C

Daftar = urutkan(A, B)
print(Daftar)
