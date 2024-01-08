'''
FILE BELAJAR
INI TIDAK TERMASUK DALAM PROGRAM KTP
JIKA TERDAPA 2 NESTING WHILE TRUE LOOP, JIKA INGIN SETELAH KELUAR DARI WHILE LOOP KEDUA, KEMUDIAN PROGRAM INGIN DI JALANKAN DARI WHILE LOOP PERTAMA DARI AWAL,
CARANYA ADALAH MEMBERIKAN PILIHAN PUTUS KEPADA KEDUA WHILE TRUE, JADI SAAT WHILE TRUE KEDUA BELUM DI PUTUS, DIA AKAN LOOPING
DI DALAM SAJA, KEMUDIAN SETELAH DI PUTUS DIA AKAN MASUK KE WHILE LOOP PERTAMA YANG DIBAWAHNYA WHILE LOOP KEUDA, PADA OPSI
PUTUS WHILE LOOP PERTAMA TERSEBUT, JIKA DI PUTUS DIA AKAN MENGAKHIRI PROGRAM, TAPI JIKA TIDAK DIPUTUS DIA AKAN MENGULANGI PROGRAM
WHILE TURE DARI AWAL DAN AKAN MASUK PADA WHILE TRUE KEDUA LAGI.
'''
while True:
    print('masuk loop 1')
    while True:
        print('masuk loop 2')
        putus = input('putus loop ke 2 : ')
        if putus in ['ya','YA','IYA','iya','Iya','Ya']:
            print('keluar dari loop 2')
            break #break akan memutus while true terdekat
        else:
            print('loop kedua diulang...')
    putus = input('putus loop ke 1 : ')
    if putus in ['ya','YA','IYA','iya','Iya','Ya']:
        print('keluar dari loop 1')
        break
    else:
        print('Loop kesatu diulang... ')
        pass
            
print('program selesai')