daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nProses semua buku dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan daftar_buku dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Titik Kosong', 3.5, -345]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda-beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Arah Langkah')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti Elemen Pertama')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
daftar_buku[0] = 'Rumah Kaca'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])