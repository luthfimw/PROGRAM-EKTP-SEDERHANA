'''
INI ADALAH FILE BELAJAR KE 2 UNTUK MENDAPATKAN IDE BAGAIMANA CARA MELAKUKAN ITERASI DENGAN MEMANGGIL INDEX PADA LIST 
BIASA YANG BUKAN NESTING LIST. CARANYA ADALAH LIST BIASA TERSEBUT DIINISIALISASI MENJADI NESTING LIST LAGI AGAR DAPAT
DIPANGGIL MENGGUNAKAN INDEXNYA, AGAR LETAK PEMANGGILAN SESUAI DENGAN YANG DIINGINKAN
'''

listk = [['hai','hallo'],['hello','apa'],[1221,121]]
while True:
    try:
        pilih = int(input('Masukkan nomor kartu Anda yang ingin dicetak : '))
        if pilih>=1 and pilih<=len(listk): #menyeleksi input user apakah nomor kartu berada dalam rentang panjang nesting list
            list_baru = listk[pilih-1] #listk[pilih-1] adalah data input user dengan index pilih-1, dimana dia ini adalah list sederhana
            baru2 = []
            baru2.append(list_baru) #list sederhana tadi dimasukkan ke dalam list lagi agar menjadi nesting list, supaya peletakkan pemanggilan anggotanya dapat sesuai keinginan.
            for i in baru2:
                    print(f'index pertama : {i[0]}')
                    print(f'index kedua : {i[1]}')
                    break #break akan selalu memutus while true terdekat
            else:
                    print('masukkan sesuai nomor kartu anda')
        else: 
             print('masukkan yang sesuai')
    except ValueError:
        print('masukkan sesuai data nomor yang didapatkan ')
    
