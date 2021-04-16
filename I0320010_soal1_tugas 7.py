#Membuat program menggunakan fungsi string
"""
Dalam perekapan pemilihan koordinator tingkat 2020 Prodi Teknik Industri Universitas X yang diikuti oleh 50 mahasiswa
dengan empat calon kandidat bernama : Yudha, Enzo, Lintang, dan Sani. Hasil pemilihan tersebut sebagai berikut: Yudha, Yudha,
Enzo, Sani, Enzo, Enzo, Enzo, Enzo, Yudha, Lintang, Yudha, Enzo, Yudha, Lintang, Sani, Sani, Yudha, Sani, Lintang, Lintang,
Sani, Sani, sani, Enzo, Sani, Yudha, Yudha, Lintang, Enzo, Sani, Yudha, Sani, Lintang, Enzo, Enzo, Sani, Enzo, Enzo, Enzo,
Lintang, Sani, Lintang, Lintang, Lintang, Sani, Yudha, Enzo, Enzo. Untuk itu buatlah program perekapan calon kandidat koordinator tingkat 2020 tersebut disertai
tampilannya yang menarik.
"""
#Program Tampilan
tampilan = "Hasil Perekapan Pemilihan Korti, Teknik Industri, Univ X"
s= tampilan.upper().center(110,'=')
print(s)

hasil = ['Yudha', 'Yudha', 'Enzo', 'Sani', 'Enzo', 'Enzo', 'Enzo', 'Enzo', 'Yudha', 'Lintang', 'Sani', 'Enzo', 'Yudha', 'Lintang', 'Yudha', 'Sani', 'Yudha', 'Sani', 'Lintang', 'Lintang', 'Sani', 'Sani', 'sani', 'Enzo', 'Sani', 'Yudha', 'Yudha', 'Lintang', 'Enzo', 'Sani', 'Yudha', 'Sani', 'Lintang', 'Enzo', 'Enzo', 'Sani', 'Enzo', 'Enzo', 'Enzo', 'Lintang', 'Sani', 'Lintang', 'Lintang', 'Lintang', 'Sani', 'Yudha', 'Enzo', 'Enzo']


print('Jumlah mahasiswa yang partisipasi :', len(hasil))
print('jumlah mahasiswa yang golput:', 50-len(hasil))

jumlah_yudha = hasil.count('Yudha')
print("\njumlah mahasiswa yang memilih Yudha sebesar ", jumlah_yudha)

jumlah_enzo = hasil.count('Enzo')
print("\njumlah mahasiswa yang memilih Enzo sebesar ", jumlah_enzo)

jumlah_sani = hasil.count('Sani')
print("\njumlah mahasiswa yang memilih Sani sebesar ", jumlah_sani)

jumlah_lintang = hasil.count('Lintang')
print("\njumlah mahasiswa yang memilih Lintang sebesar ", jumlah_lintang)

penutup= "Sekian hasil rekap, terima kasih"
tutup= penutup.center(110, "=")
print("\n", tutup)