# no_kartu_user = [1,2,3,4,5,6,7,8]
# print(f"Nomor data E-KTP yang anda miliki : ", end='')
# for i in no_kartu_user:
#     print(i, end=', ')

# listo = [None,1,2,3]
# print(f'panjang : {len(listo)}')

# while True:
#     print('ooooooo')
#     for i in range(1):
#         print('budi')
#     continue
#     print('armand')

# listp = [1,2,3,1]
# listp.clear() #clear akan menghasilkan list kosong
# print(listp)
# lisk = [1,2,3,4,2]
# pilih_nomor = int(input('Masukkan nomor kartu data E-KTP yang ingin dihapus : '))
# lisk.remove(pilih_nomor)
# print(lisk)
list_KTP = [1,2]
no_kartu_user = [1,2]
pilih_nomor = int(input('Masukkan nomor kartu data E-KTP yang ingin dihapus : '))
if pilih_nomor in range(1,len(list_KTP)+1):
    print("")
    list_KTP[pilih_nomor-1] = None #dibikin none, karena kalau di hapus, otomatis tempat list dia akan diisi oleh list_KTP[pilih_nomor-2], (cuma kegeser lah), makanya pakai none biar ga geser 
    no_kartu_user.remove(pilih_nomor)
    print(f"Data kartu dengan nomor {pilih_nomor} telah dihapus\n" )
    print(list_KTP)
    print(no_kartu_user)