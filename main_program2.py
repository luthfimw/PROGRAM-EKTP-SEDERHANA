'''
Nama : Luthfi Mahendra Widiarto
NIM  : M0122064
File python ini merupakan file utama dari program KTP yang saya buat (M0122064).
File ini harus dijalankan pada direktori yang sama pada direktori packagenya yaitu module_ktp.py
'''
from module_ktp2 import * #mengimport module yang dibutuhkan dari package_ktp
import os
os.system('cls')
list_KTP = []
no_kartu_user = []
while True:
    try:
        while True:
            menu()
            pilihan = int(input('Masukkan sesuai angka untuk program yang diinginkan : '))
            if pilihan == 1:
                if len(list_KTP)==0 and len(no_kartu_user)==0:
                    listt_KTP, noo_kartu_user = input_ktp(list_KTP,no_kartu_user)
                    list_KTP = ['diisi biar ga nge-replace'] #di beri ini supaya saat sudah keluar dari program pilihan pertama, dan saat ingin menginputakn program lagi, data yg sudah keisi tidakk tertindih
                    no_kartu_user = ['diisi biar ga nge-replace']
                else: 
                    listt_KTP, noo_kartu_user = input_ktp(listt_KTP, noo_kartu_user)
                pass
            if pilihan == 2:
                try:
                    mencetak(listt_KTP,noo_kartu_user)
                except NameError: #karena list_KTP belum terdeteksi secara global
                    print(f"\n\n{'='*75}")
                    print('Maaf, anda harus mengisikan data E-KTP pada pilihan pertama terlebih dahulu')
                    print(f"{'='*75}\n\n")
                except IndexError: 
                    print(f"\n\n{'='*79}")
                    print(f'Data dengan nomor yang anda inginkan tidak tersedia atau mungkin telah dihapus, \njika anda telah menghapusnya, silakan masukkan ulang pada pilihan 1')
                    print(f"{'='*79}\n\n")
                pass
            if pilihan == 3:
                try:
                    hapus_data(listt_KTP,noo_kartu_user)
                except NameError: #karena list_KTP belum terdeteksi secara global
                    print(f"\n\n{'='*60}")
                    print('Maaf, anda belum mengisikan data E-KTP pada pilihan pertama.')
                    print(f"{'='*60}\n\n")

                pass
            if pilihan == 4:
                program_selesai()
                break
            if pilihan not in [1,2,3,4]:
                print(f"\n\n{'='*53}")
                print('Maaf, mohon masukkan angka yang sesuai dengan pilihan')
                print(f"{'='*53}\n\n")
        break
    except ValueError:
        print(f"\n\n{'='*48}")
        print('Maaf, masukkan sesuai dengan angka yang tertera')
        print(f"{'='*48}\n\n")
        