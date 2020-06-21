from geometri.segitiga import hitung_luas_Segitiga, info as info_segitiga
from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang

print(info_segitiga())
print(f'pakai from fungsi hitung_luas_segitiga {hitung_luas_Segitiga(90,5)}')

import  geometri.segitiga
print(f'pake import fungsi hitung_luas_segitiga {geometri.segitiga.hitung_luas_Segitiga(90,7)}')

import  geometri.segitiga as gs
print(f'pake Import AS fungsi hitung_luas_segitiga {gs.hitung_luas_Segitiga(90,7)}')

print('\n Persegi Panjang')
print(info_persegipanjang())
print(f'pakai from fungsi hitung_lua_persegi_panjang {hitung_luas_persegi_panjang(90,5)}')
