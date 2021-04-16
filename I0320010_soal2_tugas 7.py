#sebuah program menggunakan nilai numerik
"""
Disajikan sebuah data sebagai berikut
a = -6.2
b =-22.74
c = 16.45
Dengan menerapkan kaidah matematika maka hitunglah:
a. Harga nilai mutlak
b. Asumsi data tersebut adalah sisi segitiga, maka berapa keliling segitiga? dengan hasil pembulatan keatas
c. jika masing masing angka dipangkatkan dengan angkanya dirinya sendiri
d. Manakah angka yang bernilai max dan minimum, syarat bahwa angka dibandingkan dalam keadaan mutlak
"""
tampilan = 'Program Penyelesaian soal'
s= tampilan.center(90,'=')
print(s)
# Harga nilai mutlak
print('\n')
a = -6.2
b =-19.74
c = 8.45

a= abs(a)
print('a =',a)

b= abs(b)
print('b =',b)

c= abs(c)
print('c =',c)

#keliling segitiga, dengan hasil pembulatan keatas
import math
keliling_seg = a + b + c
print('keliling segitiga (m) adalah ', math.ceil(keliling_seg))

#jika masing masing angka dipangkatkan dengan angkanya dirinya sendiri
print('\n')
print(a, 'pangkat', a, 'adalah', pow(a,a))
print(b, 'pangkat', b, 'adalah', pow(b,b))
print(c, 'pangkat', c, 'adalah', pow(c,c))

#max dan minim
print('\n')
print('nilai maksimum jatuh pada', max(a,b,c))
print('nilai minimum jatuh pada', min(a,b,c))
