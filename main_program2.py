'''
Nama : Luthfi Mahendra Widiarto
NIM  : M0122064
File python ini merupakan file utama dari program KTP yang saya buat (M0122064).
File ini harus dijalankan pada direktori yang sama pada direktori packagenya yaitu module_ktp.py
'''
from module_ktp2 import * #mengimport module yang dibutuhkan dari package_ktp
import os
os.system('cls')
while True:
    try:
        while True:
            menu()
            pilihan = int(input('Masukkan sesuai angka untuk program yang diinginkan : '))
            if pilihan == 1:
                list_KTP = input_ktp()
                pass
            if pilihan == 2:
                try:
                    mencetak(nik, nama, tempatlahir, tanggallahir, jeniskelamin, golongandarah, provinsi, kota, namakota, kecamatan, kelurahan, rt, rw, alamat, agama, status, pekerjaan, kewarganegaraan,masaberlaku,hariini,namkot)
                except NameError:
                    print(f"\n\n{'='*75}")
                    print('Maaf, anda harus mengisikan data E-KTP pada pilihan pertama terlebih dahulu')
                    print(f"{'='*75}\n\n")
                pass
            if pilihan == 3:
                try:
                    list_KTP,nik, nama, tempatlahir, tanggallahir, jeniskelamin, golongandarah, provinsi, kota, namakota, kecamatan, kelurahan, rt, rw, alamat, agama, status, pekerjaan, kewarganegaraan,masaberlaku,hariini,namkot=hapus_data(list_KTP,nik, nama, tempatlahir, tanggallahir, jeniskelamin, golongandarah, provinsi, kota, namakota, kecamatan, kelurahan, rt, rw, alamat, agama, status, pekerjaan, kewarganegaraan,masaberlaku,hariini,namkot)
                except NameError:
                    print(f"\n\n{'='*106}")
                    print('Maaf, anda belum mengisikan data E-KTP pada pilihan pertama. Atau anda telah berhasil menghapus data E-KTP')
                    print(f"{'='*106}\n\n")
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
        