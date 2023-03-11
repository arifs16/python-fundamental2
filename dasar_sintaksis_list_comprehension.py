print('\nPerintah del')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
del daftar_buku[0:-2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Bumi Manusia', 'Self Driving', 'Mindset', 'Basis Data']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Bumi Manusia', '2 Self Driving', '3 Mindset', '4 Basis Data']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['1 Bumi Manusia', '2 Self Driving', '3 Mindset', '4 Basis Data']
daftar_buku_baru = daftar_buku[1::2] #start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: buang diujung')
daftar_buku = ['1 Bumi Manusia', '2 Self Driving', '3 Mindset', '4 Basis Data']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Bumi Manusia', '2 Self Driving', '3 Mindset', '4 Basis Data']
print(daftar_buku[0:2])