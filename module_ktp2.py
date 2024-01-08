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
        ulang = str(input("Apakah data yang dimasukkan sudah sesuai? Ketik 'iya' jika sudah dan 'tidak' jika belum. \n"))
        while True:
                if ulang == "iya":
                        data_ktp_sementara = [hariini,nik,nama,tempatlahir,tanggallahir,jeniskelamin,golongandarah,provinsi,kota,namkot,kecamatan,kelurahan,rt,rw,alamat,agama,status,pekerjaan,kewarganegaraan,masaberlaku]
                        list_KTP.append(data_ktp_sementara)        
                        print("")
                        print(("Anda mendapatkan kartu nomor " + str(len(list_KTP))))
                        print("")
                        break
        return list_KTP

#3 FUNGIS INI DIGUNAKAN UNTUK MENCETAK DATA KTP 
def mencetak(list_KTP):
                print("")
                kartu_nomor = int(input("\nMasukkan nomor kartu Anda : "))
                print("","\nTampilkan data kartu dengan nomor", kartu_nomor, "... \n")
                print('{0}Kartu Tanda Penduduk {0}'.format(' '*27))
                print('{0}'.format('-'*70))
                print('|{0}|'.format(' '*68))
                list_KTP[0][7]='PROVINSI {}'.format(list_KTP[0][7])
                while True:
                            if (int(len(list_KTP[0][7]))%2==1):
                                list_KTP[0][7]='{0} '.format(list_KTP[0][7])
                                a=int((68-int(len(list_KTP[0][7])))/2)
                                break
                            else:
                                a=int((68-int(len(list_KTP[0][7])))/2)
                                break
                print('|{0}{1}{0}|'.format(' '*a,list_KTP[0][7]))
                namakota='{0} {1}'.format(list_KTP[0][8],namakota)
                while True:
                            if (int(len(namakota))%2==1):
                                namakota='{0} '.format(namakota)
                                b=int((68-int(len(namakota)))/2)
                                break
                            else:
                                b=int((68-int(len(namakota)))/2)
                                break
                print('|{0}{1}{0}|'.format(' '*b,namakota))
                print('|{0}|'.format(' '*68))
                list_KTP[0][1]="|  NIK               : {0}".format(list_KTP[0][1])
                print("{0}{1}|".format(list_KTP[0][1],' '*int(69-int(len(list_KTP[0][1])))))
                print('|{0}------------  |'.format(' '*54))
                nama='|  Nama              : {0}'.format(nama)
                print("{0}{1}|          |  |".format(nama,' '*int(55-int(len(nama)))))
                ttl='|  Tempat/Tgl Lahir  : {0}, {1}'.format(tempatlahir,tanggallahir)
                print("{0}{1}|          |  |".format(ttl,' '*int(55-int(len(ttl)))))
                jeniskelamin='|  Jenis kelamin     : {0}'.format(jeniskelamin)
                golongandarah='      Gol. Darah  : {0}'.format(golongandarah)
                jekgol=int(len(jeniskelamin))+int(len(golongandarah))
                print('{0}{1}{2}|          |  |'.format(jeniskelamin,golongandarah,' '*int(55-int(jekgol))))
                alamat='|  Alamat            : {0}'.format(alamat)
                print("{0}{1}|          |  |".format(alamat,' '*int(55-int(len(alamat)))))
                rtrw='|      RT/RW         : {0}/{1}'.format(rt,rw)
                print('{0}{1}|   FOTO   |  |'.format(rtrw,' '*int(55-int(len(rtrw)))))
                kelurahan="|      Kel/Desa      : {0}".format(kelurahan)
                print('{0}{1}|          |  |'.format(kelurahan,' '*int(55-int(len(kelurahan)))))
                kecamatan="|      Kecamatan     : {0}".format(kecamatan)
                print('{0}{1}|          |  |'.format(kecamatan,' '*int(55-int(len(kecamatan)))))
                agama="|  Agama             : {0}".format(agama)
                print("{0}{1}|          |  |".format(agama,' '*int(55-int(len(agama)))))
                status="|  Status Perkawinan : {0}".format(status)
                print("{0}{1}------------  |".format(status,' '*int(55-int(len(status)))))
                pekerjaan="|  Pekerjaan         : {0}".format(pekerjaan)
                while True:
                            if (int(len(namkot))%2==1):
                                namkot='{0} '.format(namkot)
                                c=int((16-int(len(namkot)))/2)
                                break
                            else:
                                c=int((16-int(len(namkot)))/2)
                                break
                print("{0}{1}{2}{3}{2}|".format(pekerjaan,' '*int(53-int(len(pekerjaan))),' '*c,namkot))
                kewarganegaraan="|  Kewarganegaraan   : {0}".format(kewarganegaraan)
                print("{0}{1} {2}   |".format(kewarganegaraan,' '*int(55-int(len(kewarganegaraan))),hariini))
                masaberlaku="|  Berlaku Hingga    : {0}".format(masaberlaku)
                print("{0}{1}|".format(masaberlaku,' '*int(69-int(len(masaberlaku)))))
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
                dataa.write('|{0}{1}{0}|'.format(' '*a,list_KTP[0][7])+'\n')        
                dataa.write('|{0}{1}{0}|'.format(' '*b,namakota)+'\n')
                dataa.write('|{0}|'.format(' '*68)+'\n')
                dataa.write("{0}{1}|".format(list_KTP[0][1],' '*int(69-int(len(list_KTP[0][1]))))+'\n')
                dataa.write('|{0}------------  |'.format(' '*54)+'\n')    
                dataa.write("{0}{1}|          |  |".format(nama,' '*int(55-int(len(nama))))+'\n') 
                dataa.write("{0}{1}|          |  |".format(ttl,' '*int(55-int(len(ttl))))+'\n')     
                dataa.write('{0}{1}{2}|          |  |'.format(jeniskelamin,golongandarah,' '*int(55-int(jekgol)))+'\n')     
                dataa.write("{0}{1}|          |  |".format(alamat,' '*int(55-int(len(alamat))))+'\n')   
                dataa.write('{0}{1}|   FOTO   |  |'.format(rtrw,' '*int(55-int(len(rtrw))))+'\n')  
                dataa.write('{0}{1}|          |  |'.format(kelurahan,' '*int(55-int(len(kelurahan))))+'\n')  
                dataa.write('{0}{1}|          |  |'.format(kecamatan,' '*int(55-int(len(kecamatan))))+'\n')
                dataa.write("{0}{1}|          |  |".format(agama,' '*int(55-int(len(agama))))+'\n')
                dataa.write("{0}{1}------------  |".format(status,' '*int(55-int(len(status))))+'\n')
                dataa.write("{0}{1}{2}{3}{2}|".format(pekerjaan,' '*int(53-int(len(pekerjaan))),' '*c,namkot)+'\n') 
                dataa.write("{0}{1} {2}   |".format(kewarganegaraan,' '*int(55-int(len(kewarganegaraan))),hariini)+'\n')
                dataa.write("{0}{1}|".format(masaberlaku,' '*int(69-int(len(masaberlaku))))+'\n')
                dataa.write('|{0}|'.format(' '*68)+'\n')
                dataa.write('|{0}|'.format(' '*68)+'\n')
                dataa.write('|{0}TTD       |'.format(' '*58)+'\n')
                dataa.write('|{0}|'.format(' '*68)+'\n')
                dataa.write('-'*70+'\n')
        
#4 FUGNSI INI UNTUK MENGHAPUS DATA E-KTP YANG SUDAH DI BUAT
def hapus_data(list_KTP,nik, nama, tempatlahir, tanggallahir, jeniskelamin, golongandarah, provinsi, kota, namakota, kecamatan, kelurahan, rt, rw, alamat, agama, status, pekerjaan, kewarganegaraan, masaberlaku, hariini,namkot):
        kartu_nomor = int(input("\nMasukkan nomor kartu anda : "))
        print("")
        # list_KTP[kartu_nomor-1] = None
        list_KTP.clear()
        print("Data kartu dengan nomor " + str(kartu_nomor) + " telah dihapus", "\n")
        del nik
        del nama
        del tempatlahir
        del tanggallahir
        del jeniskelamin
        del golongandarah
        del provinsi
        del golongandarah
        del kota
        del namakota
        del kecamatan
        del kelurahan
        del rt
        del rw
        del alamat
        del agama
        del status
        del pekerjaan
        del kewarganegaraan
        del masaberlaku
        del hariini
        del namkot
        return list_KTP, nik, nama, tempatlahir, tanggallahir, jeniskelamin, golongandarah, provinsi, kota, namakota, kecamatan, kelurahan, rt, rw, alamat, agama, status, pekerjaan, kewarganegaraan,masaberlaku,hariini,namkot
        
        
        
#5 UNTUK KELUAR DARI PROGRAM
def program_selesai():
        while True: 
                print()
                print(f"\n{'='*50}")
                print("ANDA KELUAR DARI PROGRAM".center(50))
                print('TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI'.center(50))
                print(f'{"="*25}{"="*25}\n')
                break