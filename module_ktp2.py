'''
Nama : Luthfi Mahendra Widiarto
NIM  : M0122064
ini adalah modul atau package yang berisi deklarasi fungsi untuk digunakan pada program utama ktp yaitu main_ktp.py
yang berada di dalam satu folder dengan file module ini.
'''

#1 FUNGSI UNTUK MEMBERIKAN PILIHAN FITUR PADA PROGRAM INPUT E-KTP
def menu ():
        '''Menampilakn fitur yang tersedia pada program E-KTP'''
        print(f"{'='*10} Selamat Datang di Program E-KTP {'='*10}")
        print("\n\t   DAFTAR MENU")
        print("     [1] Input Data E-KTP")
        print("     [2] Cetak Data E-KTP")
        print("     [3] Hapus Data E-KTP")
        print("     [4] Keluar dari Program")

#2 FUGNSI JIKA PILIHAN YANG DIPILIH ADALAH INPUT DATA UNTUK E-KTP
def input_ktp():
        '''Panggil fungsi ini jika yang dipilih adalah nomor [1]'''
        list_KTP = []
        import datetime
        waktu=datetime.date.today()
        year=waktu.year
        month=waktu.month
        day=waktu.day
        while True:
                if day<10:
                        day='0{0}'.format(day)
                        if month<10:
                                month='0{0}'.format(month)
                                break
                        else:
                                month=month
                                break
                        break
                else:
                        if month<10:
                                month='0{0}'.format(month)
                                break
                
                        else:
                                month=month
                                break
                        day=day
                        break
        hariini='{0}-{1}-{2}'.format(day,month,year)
        
        while True: #while true utama, PENTING UNTUK AKHIR 
                print("\nSilakan input data E-KTP dengan benar")
                while True:
                        try:
                                nik=int(input('NIK \t\t\t   : '))
                                digit=len(str(abs(nik)))
                                while (digit!=16): 
                                        print ('NIK salah, mohon masukkan 16 digit angka NIK dengan benar')
                                        nik=int(input('NIK \t\t\t   : '))
                                        digit=len(str(abs(nik)))
                                break
                        except ValueError:
                                print('NIK salah, mohon masukkan 16 digit angka NIK dengan benar')
                                pass

                nama=str(input('Nama Lengkap \t\t   : '))
                nama=nama.upper()
                tempatlahir=str(input('Tempat Lahir \t\t   : '))
                tempatlahir=tempatlahir.upper()
                
                while True:
                        try:
                                tanggallahir=input('Tanggal Lahir (DDMMYYYY)   : ')
                                tanggallahir=datetime.datetime.strptime(tanggallahir, '%d%m%Y')
                                hari=tanggallahir.day
                                bulan=tanggallahir.month
                                tahun=tanggallahir.year
                
                                while True:     
                                        if hari<10:
                                                hari='0{0}'.format(hari)
                                                if bulan<10:
                                                        bulan='0{0}'.format(bulan)
                                                        break
                                                else:
                                                        bulan=bulan
                                                break
                                        
                                        else:
                                                if bulan<10:
                                                        bulan='0{0}'.format(bulan)
                                                        break
                                        
                                                else:
                                                        bulan=bulan
                                                        break
                                                hari=hari
                                                break
                                tanggallahir='{0}-{1}-{2}'.format(hari,bulan,tahun)
                                break
                        except ValueError:
                                print('Mohon masukkan angka yang sesuai dengan tanggal lahir anda')
                                
                while True:
                        jeniskelamin=str(input('Jenis Kelamin (pilih L/P)  : '))
                        if jeniskelamin in ['L', 'l']:
                                jeniskelamin='LAKI-LAKI'
                                break
                        elif jeniskelamin in ['P','p']:
                                jeniskelamin='PEREMPUAN'
                                break
                        print('Maaf hanya menerima laki-laki atau perempuan. Silahkan masukkan ulang (L/P)')
                while True:
                        print(f'Pilih golongan darah anda\nO\nA\nB\nAB')
                        golongandarah=str(input('Golongan Darah \t\t   : '))
                        if golongandarah in ['A', 'a']:
                                golongandarah='A'
                                break
                        elif golongandarah in ['B','b']:
                                golongandarah='B'
                                break
                        elif golongandarah in ['O','o']:
                                golongandarah='O'
                                break
                        elif golongandarah in ['AB','Ab','aB','ab']:
                                golongandarah='AB'
                                break
                        print('Golongan Darah tidak ditemukan. Silahkan masukkan ulang. Contoh, Golongan Darah : O')
                provinsi=str(input('Provinsi \t\t   : '))
                provinsi=provinsi.upper()
                while True:
                                kota=str(input('Kabupaten/Kota (pilih 1/2) : '))
                                if kota=='1':
                                        kota='KABUPATEN'
                                        namakota=str(input('Nama Kabupaten \t\t   : '))
                                        namakota=namakota.upper()
                                        namkot=namakota
                                        break
                                elif kota=='2':
                                        kota='KOTA'
                                        namakota=str(input('Nama Kota \t\t   : '))
                                        namakota=namakota.upper()
                                        namkot=namakota
                                        break
                                print('Pilih Kabupaten atau Kota dengan benar. Silahkan masukkan ulang (1/2)')
                kecamatan=str(input('Kecamatan \t\t   : '))
                kecamatan=kecamatan.upper()
                kelurahan=str(input('Kelurahan/Desa \t\t   : '))
                kelurahan=kelurahan.upper()    
                while True:
                        rt=input('RT (dalam angka) \t   : ')
                        rw=input('RW (dalam angka) \t   : ')
                        if len(rt) < 3 or len(rw) < 3:
                                print('Anda harus memasukkan 3 digit atau lebih untuk rt dan rw.')
                        else:
                                break
                        
                alamat=str(input('Alamat \t\t\t   : '))
                alamat=alamat.upper()
                agama=str(input('Agama \t\t\t   : '))
                agama=agama.upper()
                status=str(input('Status Perkawinan \t   : '))
                status=status.upper()
                pekerjaan=str(input('Pekerjaan \t\t   : '))
                pekerjaan=pekerjaan.upper()
                while True:
                        kewarganegaraan=str(input('Kewarganegaraan \t   : '))
                        if kewarganegaraan in ['Indonesia','indonesia','INDONESIA','wni','WNI']:
                                kewarganegaraan='WNI'
                                masaberlaku='SEUMUR HIDUP'
                                break
                        else :
                                kewarganegaraan=kewarganegaraan.upper()
                                year+=5
                                masaberlaku='{0}-{1}-{2}'.format(day,month,year)
                                break
                print()
                while True:
                        ulang = str(input("Apakah data yang dimasukkan sudah sesuai? Ketik 'iya' jika sudah dan 'tidak' jika belum. \n"))
                        if ulang in ["iya","IYA","Iya","ya","YA","Ya"]: #jika memilih 'iya' , maka data akan disimpan dalam list, jika kemudian ingin menambahkan data lagi, dia bisa menyimpan data baru tersebut di dalam nesting list.
                                data_ktp_sementara = [hariini,nik,nama,tempatlahir,tanggallahir,jeniskelamin,golongandarah,provinsi,kota,namkot,kecamatan,kelurahan,rt,rw,alamat,agama,status,pekerjaan,kewarganegaraan,masaberlaku,namakota]
                                list_KTP.append(data_ktp_sementara)        
                                print("")
                                print(("Anda mendapatkan kartu nomor " + str(len(list_KTP))))
                                print("")
                                break
                                
                        elif ulang in ["tidak","Tidak","TIDAK","TDK","tdk","Tdk"]: #jika memilih 'tidak', otomatis data tidak akan tersimpan dan jika mengisi lagi maka data sebelumnya akan ditimpa.
                                print('\nSilahkan masukkan data ktp lagi...')
                                break
                pilihan_loop_utama = input('Apakah anda ingin memasukkan data ktp lainnya atau ingin memasukkan ulang? Ketik "iya" jika setuju atau ketik "tidak" jika tidak setuju... \n')
                if pilihan_loop_utama in ["tidak","Tidak","TIDAK","TDK","tdk","Tdk"]:
                        break #jika memilih ini, maka program while true utama akan di putus dan meretrun list_KTP
                else:
                        pass #pass disini akan mengembalikan while true ke atas dan menjalankan program dari awal lagi pada input data ktp.
        return list_KTP #menyimpan data yang telah diinputkan.

#3 FUNGIS INI DIGUNAKAN UNTUK MENCETAK DATA KTP 
def mencetak(list_KTP):
                while True:
                        try:
                                kartu_nomor = int(input("\nMasukkan nomor kartu yang ingin dicetak : "))
                                if kartu_nomor>=1 and kartu_nomor<=len(list_KTP):
                                        list_inisialisai = list_KTP[kartu_nomor-1]
                                        list_mencetak_spesifik = []
                                        list_mencetak_spesifik.append(list_inisialisai)
                                        for i in list_mencetak_spesifik:
                                                print("")
                                                print("","\nTampilkan data kartu dengan nomor", kartu_nomor, "... \n")
                                                print('{0}Kartu Tanda Penduduk {0}'.format(' '*27))
                                                print('{0}'.format('-'*70))
                                                print('|{0}|'.format(' '*68))
                                                i[7]='PROVINSI {}'.format(i[7])
                                                while True:
                                                        if (int(len(i[7]))%2==1):
                                                                i[7]='{0} '.format(i[7])
                                                                a=int((68-int(len(i[7])))/2)
                                                                break
                                                        else:
                                                                a=int((68-int(len(i[7])))/2)
                                                                break
                                                print('|{0}{1}{0}|'.format(' '*a,i[7]))
                                                i[20]='{0} {1}'.format(i[8],i[20])
                                                while True:
                                                        if (int(len(i[20]))%2==1):
                                                                i[20]='{0} '.format(i[20])
                                                                b=int((68-int(len(i[20])))/2)
                                                                break
                                                        else:
                                                                b=int((68-int(len(i[20])))/2)
                                                                break
                                                print('|{0}{1}{0}|'.format(' '*b,i[20]))
                                                print('|{0}|'.format(' '*68))
                                                i[1]="|  NIK               : {0}".format(i[1])
                                                print("{0}{1}|".format(i[1],' '*int(69-int(len(i[1])))))
                                                print('|{0}------------  |'.format(' '*54))
                                                i[2]='|  Nama              : {0}'.format(i[2])
                                                print("{0}{1}|          |  |".format(i[2],' '*int(55-int(len(i[2])))))
                                                ttl='|  Tempat/Tgl Lahir  : {0}, {1}'.format(i[3],i[4])
                                                print("{0}{1}|          |  |".format(ttl,' '*int(55-int(len(ttl)))))
                                                i[5]='|  Jenis kelamin     : {0}'.format(i[5])
                                                i[6]='      Gol. Darah  : {0}'.format(i[6])
                                                jekgol=int(len(i[5]))+int(len(i[6]))
                                                print('{0}{1}{2}|          |  |'.format(i[5],i[6],' '*int(55-int(jekgol))))
                                                i[14]='|  Alamat            : {0}'.format(i[14])
                                                print("{0}{1}|          |  |".format(i[14],' '*int(55-int(len(i[14])))))
                                                rtrw='|      RT/RW         : {0}/{1}'.format(i[12],i[13])
                                                print('{0}{1}|   FOTO   |  |'.format(rtrw,' '*int(55-int(len(rtrw)))))
                                                i[11]="|      Kel/Desa      : {0}".format(i[11])
                                                print('{0}{1}|          |  |'.format(i[11],' '*int(55-int(len(i[11])))))
                                                i[10]="|      Kecamatan     : {0}".format(i[10])
                                                print('{0}{1}|          |  |'.format(i[10],' '*int(55-int(len(i[10])))))
                                                i[15]="|  Agama             : {0}".format(i[15])
                                                print("{0}{1}|          |  |".format(i[15],' '*int(55-int(len(i[15])))))
                                                i[16]="|  Status Perkawinan : {0}".format(i[16])
                                                print("{0}{1}------------  |".format(i[16],' '*int(55-int(len(i[16])))))
                                                i[17]="|  Pekerjaan         : {0}".format(i[17])
                                                while True:
                                                        if (int(len(i[9]))%2==1):
                                                                i[9]='{0} '.format(i[9])
                                                                c=int((16-int(len(i[9])))/2)
                                                                break
                                                        else:
                                                                c=int((16-int(len(i[9])))/2)
                                                                break
                                                print("{0}{1}{2}{3}{2}|".format(i[17],' '*int(53-int(len(i[17]))),' '*c,i[9]))
                                                i[18]="|  Kewarganegaraan   : {0}".format(i[18])
                                                print("{0}{1} {2}   |".format(i[18],' '*int(55-int(len(i[18]))),i[0]))
                                                i[19]="|  Berlaku Hingga    : {0}".format(i[19])
                                                print("{0}{1}|".format(i[19],' '*int(69-int(len(i[19])))))
                                                print('|{0}|'.format(' '*68))
                                                print('|{0}|'.format(' '*68))
                                                print('|{0}TTD       |'.format(' '*58))
                                                print('|{0}|'.format(' '*68))
                                                print('-'*70)               
                                #KODE DI BAWAH INI UNTUK MENAMPILKAN DI NOTEPAD
                                                dataa = open('output_ktp_M0122064.txt',"a")
                                                dataa.write('{0}Kartu Tanda Penduduk {0}'.format(' '*25)+'\n')
                                                dataa.write('{0}'.format('-'*70)+'\n')
                                                dataa.write('|{0}|'.format(' '*68)+'\n')        
                                                dataa.write('|{0}{1}{0}|'.format(' '*a,i[7])+'\n')        
                                                dataa.write('|{0}{1}{0}|'.format(' '*b,i[20])+'\n')
                                                dataa.write('|{0}|'.format(' '*68)+'\n')
                                                dataa.write("{0}{1}|".format(i[1],' '*int(69-int(len(i[1]))))+'\n')
                                                dataa.write('|{0}------------  |'.format(' '*54)+'\n')    
                                                dataa.write("{0}{1}|          |  |".format(i[1],' '*int(55-int(len(i[1]))))+'\n') 
                                                dataa.write("{0}{1}|          |  |".format(ttl,' '*int(55-int(len(ttl))))+'\n')     
                                                dataa.write('{0}{1}{2}|          |  |'.format(i[5],i[6],' '*int(55-int(jekgol)))+'\n')     
                                                dataa.write("{0}{1}|          |  |".format(i[14],' '*int(55-int(len(i[14]))))+'\n')   
                                                dataa.write('{0}{1}|   FOTO   |  |'.format(rtrw,' '*int(55-int(len(rtrw))))+'\n')  
                                                dataa.write('{0}{1}|          |  |'.format(i[11],' '*int(55-int(len(i[11]))))+'\n')  
                                                dataa.write('{0}{1}|          |  |'.format(i[10],' '*int(55-int(len(i[10]))))+'\n')
                                                dataa.write("{0}{1}|          |  |".format(i[15],' '*int(55-int(len(i[15]))))+'\n')
                                                dataa.write("{0}{1}------------  |".format(i[16],' '*int(55-int(len(i[16]))))+'\n')
                                                dataa.write("{0}{1}{2}{3}{2}|".format(i[17],' '*int(53-int(len(i[17]))),' '*c,i[9])+'\n') 
                                                dataa.write("{0}{1} {2}   |".format(i[18],' '*int(55-int(len(i[18]))),i[0])+'\n')
                                                dataa.write("{0}{1}|".format(i[19],' '*int(69-int(len(i[19]))))+'\n')
                                                dataa.write('|{0}|'.format(' '*68)+'\n')
                                                dataa.write('|{0}|'.format(' '*68)+'\n')
                                                dataa.write('|{0}TTD       |'.format(' '*58)+'\n')
                                                dataa.write('|{0}|'.format(' '*68)+'\n')
                                                dataa.write('-'*70+'\n')
                                else:
                                        print('Masukkan nomor data E-KTP sesuai yang anda dapatkan!')
                        except ValueError:
                                print('Mohon masukkan nomor KTP dengan benar')
#4 FUGNSI INI UNTUK MENGHAPUS DATA E-KTP YANG SUDAH DI BUAT
def hapus_data(list_KTP):
        kartu_nomor = int(input("\nMasukkan nomor kartu anda : "))
        print("")
        # list_KTP[kartu_nomor-1] = None
        list_KTP.clear()
        print("Data kartu dengan nomor " + str(kartu_nomor) + " telah dihapus", "\n")   
        
#5 UNTUK KELUAR DARI PROGRAM
def program_selesai():
        while True: 
                print()
                print(f"\n{'='*50}")
                print("ANDA KELUAR DARI PROGRAM".center(50))
                print('TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI'.center(50))
                print(f'{"="*25}{"="*25}\n')
                break