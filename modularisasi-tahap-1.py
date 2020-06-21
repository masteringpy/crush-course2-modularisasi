"""
program menghitung luas segitiga
luas_segitiga = alas * tinggi /2

"""
print('Menghitung Luas segitiga 1')

alas = 10
tinggi = 6
luas_Segitiga = alas * tinggi / 2
print(f' segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_Segitiga}')

alas = 20
tinggi = 5
luas_Segitiga = alas * tinggi / 2
print(f' segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_Segitiga}')

print('\n Menghitung Luas segitiga 2 copas ')
print(f' segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_Segitiga}')

print('\n membuat fungsi hitung_luas_segitiga')
def hitung_luas_Segitiga(alas, tinggi):
    luas_Segitiga = alas * tinggi / 2
    return luas_Segitiga

print(f' menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_Segitiga(10, 6)}')
print(f' menghitung luas segitiga dengan dungsi hasilnya = {hitung_luas_Segitiga(60, 2)}')
print(f' menghitung luas segitiga alas= {alas} dan tinggi= {tinggi} dengan dungsi hasilnya = {hitung_luas_Segitiga(60, 2)}')


