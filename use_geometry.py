from geometry.persegipanjang import hitung_luas_persegipanjang, info as info_persegipanjang
from geometry.segitiga import hitung_luas_segitiga, info as info_segitiga

print(f'\n{info_segitiga()}')
print(f'Luas segitiga {hitung_luas_segitiga(10, 5)}')

print(f'\n{info_persegipanjang()}')
print(f'Luas Persegi Panjang {hitung_luas_persegipanjang(10, 5)}')
