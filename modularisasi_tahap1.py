"""
Program menghitung luas segitiga
luas = alas * tinggi / 2
"""
print('\nMenghitung luas segitiga')
alas = 10
tinggi = 5
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung luas segitiga dengan copy paste')
alas = 9
tinggi = 7
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi hitung luas segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 5
print(f'Luas segitiga = {hitung_luas_segitiga(10, 5)}')
print(f'Luas segitiga = {hitung_luas_segitiga(9, 7)}')
print(f'Luas segitiga dengan alas={alas} dan tinggi={tinggi} adalah {hitung_luas_segitiga(alas, tinggi)}')





