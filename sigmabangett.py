import os

terminal_width = os.get_terminal_size().columns
print("✰ ~ ❀ ◦ ☾ ❄ " * terminal_width)
print()
print()

from pyfiglet import figlet_format

text = figlet_format("zigma shop", font="ansi_shadow")
terminal_width = os.get_terminal_size().columns
text_width = len(text.splitlines()[0])
spasi = (terminal_width - text_width) // 2
centered_text = '\n'.join((' ' * spasi + line) for line in text.splitlines())

print(centered_text)

terminal_width = os.get_terminal_size().columns
print("✰ ~ ❀ ◦ ☾ ❄ " * terminal_width)

    
print(f"{"       "*8}SELAMAT DATANG DI TOKO KAMI, ZIGMA SHOP ;) tekan [ENTER] untuk melanjutkan >>>")
input()

kasir = {
    "Aiz": "marklee",
    "Puput": "kyungsoo",
}

def login():
    print("==========SELAMAT DATANG! LOG IN DULU DUNGS========")
    while True :
        global username
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        
        if username in kasir and kasir[username] == password:
            print("Login berhasil! Selamat datang, Kasir {}!".format(username))
            return
        else:
            print("Username atau password salah. Silakan coba lagi.")


stok = {
    "celana kulot": 0,
    "celana formal": 0,
    "celana cargo": 0,
    "kemeja flanel": 0,
    "kemeja denim": 0,
    "kemeja linen": 0,
    "rok plisket": 0,
    "rok a line": 0,
    "rok span": 0,
    "kaos kerah": 0,
    "kaos rib": 0,
    "kaos oversize": 0,
    "pashmina": 0,
    "hijab instan": 0,
    "segiempat": 0,
    "cardigan": 0,
    "jaket kulit": 0,
    "jaket parasut": 0
}

def tambahkan_stok():
    global stok
    print()
    print("============== MANAJEMEN STOK ===================")
    stok_baru = {
        "celana kulot": int(input("Masukkan stok celana kulot: ")),
        "celana formal": int(input("Masukkan stok celana formal: ")),
        "celana cargo": int(input("Masukkan stok celana cargo: ")),
        "kemeja flanel": int(input("Masukkan stok kemeja flanel: ")),
        "kemeja denim": int(input("Masukkan stok kemeja denim: ")),
        "kemeja linen": int(input("Masukkan stok kemeja linen: ")),
        "rok plisket": int(input("Masukkan stok rok plisket: ")),
        "rok a line": int(input("Masukkan stok rok a line: ")),
        "rok span": int(input("Masukkan stok rok span: ")),
        "kaos kerah": int(input("Masukkan stok kaos kerah: ")),
        "kaos rib": int(input("Masukkan stok kaos rib: ")),
        "kaos oversize": int(input("Masukkan stok kaos oversize: ")),
        "pashmina": int(input("Masukkan stok hijab pashmina: ")),
        "hijab instan": int(input("Masukkan stok hijab instan: ")),
        "segiempat": int(input("Masukkan stok hijab segiempat: ")),
        "cardigan": int(input("Masukkan stok cardigan: ")),
        "jaket kulit": int(input("Masukkan stok jaket kulit: ")),
        "jaket parasut": int(input("Masukkan stok jaket parasut: "))
    }
    
    for item, jumlah in stok_baru.items():
        stok[item] += jumlah
    
    print("Stok telah ditambahkan.")

def jenis_produk():
    global jumlah  
    pembelian = []
    jumlah = 0  
    while True:
        print('''
            Jenis - Jenis Produk :
            1. Celana
            2. Kemeja
            3. Rok
            4. Kaos
            5. Hijab
            6. Jaket
            7. Selesai''')

        pilih = input("Pilih Jenis Produk (1-7) : ")

        if pilih == '1':
            print(''' 
            ================== JENIS CELANA ===============
            |  No. |    Jenis      |     Harga    |  Stok    
            |  1.  | Celana Kulot  | Rp. 38.000,- |  {}    
            |  2.  | Celana Formal | Rp. 43.000,- |  {}    
            |  3.  | Celana Cargo  | Rp. 54.000,- |  {}    
            ==============================================='''.format(stok['celana kulot'], stok['celana formal'], stok['celana cargo']))

            choose = input("Pilih Jenis Celana (1-3) : ")
            potong = int(input("Berapa Potong Celana : "))

            if choose == '1' and stok['celana kulot'] >= potong:
                jumlah += potong * 38000
                stok['celana kulot'] -= potong
                pembelian.append(f"celana kulot x {potong} - Rp. {potong * 38000}")
            elif choose == '2' and stok['celana formal'] >= potong:
                jumlah += potong * 43000
                stok['celana formal'] -= potong
                pembelian.append(f"celana formal x {potong} - Rp. {potong * 43000}")
            elif choose == '3' and stok['celana cargo'] >= potong:
                jumlah += potong * 54000
                stok['celana cargo'] -= potong
                pembelian.append(f"celana cargo x {potong} - Rp. {potong * 54000}")
            else:
                print("Stok tidak cukup atau pilihan salah. Coba Lagi.")

        elif pilih == '2':
            print('''
            ================ JENIS KEMEJA ================
            |  No. |    Jenis      |     Harga    |  Stok
            |  1.  | Kemeja Flanel | Rp. 52.000,- |  {}
            |  2.  | Kemeja Denim  | Rp. 65.000,- |  {}
            |  3.  | Kemeja Linen  | Rp. 44.000,- |  {}
            =============================================='''.format(stok['kemeja flanel'], stok['kemeja denim'], stok['kemeja linen']))


            choose = input("Pilih Jenis Kemeja (1-3) : ")
            potong = int(input("Berapa Potong Kemeja: "))

            if choose == '1' and stok['kemeja flanel'] >= potong:
                jumlah += potong * 52000
                stok['kemeja flanel'] -= potong
                pembelian.append(f"Kemeja Flanel x {potong} - Rp. {potong * 52000}")
            elif choose == '2' and stok['kemeja denim'] >= potong:
                jumlah += potong * 65000
                stok['kemeja denim'] -= potong
                pembelian.append(f"Kemeja Denim x {potong} - Rp. {potong * 65000}")
            elif choose == '3' and stok['kemeja linen'] >= potong:
                jumlah += potong * 44000
                stok['kemeja linen'] -= potong
                pembelian.append(f"Kemeja Linen x {potong} - Rp. {potong * 44000}")
            else :
                print("Stok tidak cukup atau pilihan salah. Coba Lagi.")

        elif pilih == '3':
            print('''
            ================== JENIS ROK =================
            |  No. |    Jenis      |     Harga    |  Stok 
            |  1.  | Rok Plisket   | Rp. 32.000,- |  {}
            |  2.  | Rok A line    | Rp. 53.000,- |  {}
            |  3.  | Rok Span      | Rp. 38.000,- |  {}
            =============================================='''.format(stok['rok plisket'], stok['rok a line'], stok['rok span']))


            choose = input("Pilih Jenis Rok (1-3) : ")
            potong = int(input("Berapa Potong Rok : "))

            if choose == '1'and stok['rok plisket'] >= potong:
                jumlah += potong * 32000
                stok['rok plisket'] -= potong
                pembelian.append(f"Rok Plisket x {potong} - Rp. {potong * 32000}")
            elif choose == '2' and stok['rok a line'] >= potong:
                jumlah += potong * 53000
                stok['rok a line'] -= potong
                pembelian.append(f"Rok A line x {potong} - Rp. {potong * 53000}")
            elif choose == '3' and stok['rok span'] >= potong:
                jumlah += potong * 38000
                stok['rok span'] -= potong
                pembelian.append(f"Rok Span x {potong} - Rp. {potong * 38000}")
            else :
                print("Stok tidak cukup atau pilihan salah. Coba Lagi")

        elif pilih == '4':
            print('''
            ================== JENIS KAOS =================
            |  No. |    Jenis       |     Harga    |  Stok
            |  1.  | Kaos Kerah     | Rp. 55.000,- |  {}
            |  2.  | Kaos Rib       | Rp. 47.000,- |  {}
            |  3.  | Kaos Oversize  | Rp. 46.000,- |  {}
            ==============================================='''.format(stok['kaos kerah'], stok['kaos rib'], stok['kaos oversize']))
 

            choose = input("Pilih Jenis Kaos (1-3) : ")
            potong = int(input("Berapa Potong Kaos : "))

            if choose == '1' and stok['kaos kerah'] >= potong:
                jumlah += potong * 55000
                stok['kaos kerah'] -= potong
                pembelian.append(f"Kaos Kerah x {potong} - Rp. {potong * 55000}")
            elif choose == '2'and stok['kaos rib'] >= potong:
                jumlah += potong * 47000
                stok['kaos rib'] -= potong
                pembelian.append(f"Kaos Rib x {potong} - Rp. {potong * 47000}")
            elif choose == '3' and stok['kaos oversize'] >= potong:
                jumlah += potong * 46000
                stok['kaos oversize'] -= potong
                pembelian.append(f"Kaos Oversize x {potong} - Rp. {potong * 46000}")
            else :
                print("Stok tidak cukup atau pilihan salah. Coba Lagi")

        elif pilih == '5':
            print('''
            ================== JENIS HIJAB ===============
            |  No. |    Jenis      |     Harga    |  Stok
            |  1.  | Pashmina      | Rp. 20.000,- |  {}
            |  2.  | Hijab Instan  | Rp. 18.000,- |  {}
            |  3.  | Segiempat     | Rp. 15.000,- |  {}
            ==============================================='''.format(stok['pashmina'], stok['hijab instan'], stok['segiempat']))  

            choose = input("Pilih Jenis Hijab (1-3) : ")
            potong = int(input("Berapa Potong Hijab : "))

            if choose == '1' and stok['pashmina'] >= potong:
                jumlah += potong * 20000
                stok['pashmina'] -= potong
                pembelian.append(f"Pashmina x {potong} - Rp. {potong * 20000}")
            elif choose == '2' and stok['hijab instan'] >= potong:
                jumlah += potong * 18000
                stok['hijab instan'] -= potong
                pembelian.append(f"Hijab Instan x {potong} - Rp. {potong * 18000}")
            elif choose == '3' and stok['segiempat'] >= potong:
                jumlah += potong * 15000
                stok['segiempat'] -= potong
                pembelian.append(f"Segiempat x {potong} - Rp. {potong * 15000}")
            else :
                print("Stok tidak cukup atau pilihan salah. Coba Lagi")

        elif pilih == '6':
            print('''
            ================== JENIS JAKET ===============
            |  No. |    Jenis      |     Harga    |  Stok
            |  1.  | Cardigan      | Rp. 55.000,- |  {}
            |  2.  | Jaket Kulit   | Rp. 98.000,- |  {}
            |  3.  | Jaket Parasut | Rp. 92.000,- |  {}
            =============================================='''.format(stok['cardigan'], stok['jaket kulit'], stok['jaket parasut']))  

            choose = input("Pilih Jenis Jaket (1-3) : ")
            potong = int(input("Berapa Potong Jaket : "))

            if choose == '1' and stok['cardigan'] >= potong:
                jumlah += potong * 55000
                stok['cardigan'] -= potong
                pembelian.append(f"Cardigan x {potong} - Rp. {potong * 55000}")
            elif choose == '2' and stok['jaket kulit'] >= potong:
                jumlah += potong * 98000
                stok['jaket kulit'] -= potong
                pembelian.append(f"Jaket Kulit x {potong} - Rp. {potong * 98000}")
            elif choose == '3' and stok['jaket parasut'] >= potong:
                jumlah += potong * 92000
                stok['jaket parasut'] -= potong
                pembelian.append(f"Jaket Parasut x {potong} - Rp. {potong * 92000}")
            else :
                print("Stok tidak cukup atau pilihan salah. Coba Lagi")

        elif pilih == '7':
            print("Barang Telah di Data.\n")
            break
        else:
            print("Pilihan Anda Salah. Silahkan Pilih Ulang.")

    return pembelian, jumlah

def tampilkan_stok():
    print('''
    ====================== TOTAL STOK =========================
    |  No. |    Jenis Produk     |  Stok Tersedia            |
    |  1.  | Celana Kulot        |  {}                        |
    |  2.  | Celana Formal       |  {}                        |
    |  3.  | Celana Cargo        |  {}                        |
    |  4.  | Kemeja Flanel       |  {}                        |
    |  5.  | Kemeja Denim        |  {}                        |
    |  6.  | Kemeja Linen        |  {}                        |
    |  7.  | Rok Plisket         |  {}                        |
    |  8.  | Rok A Line          |  {}                        |
    |  9.  | Rok Span            |  {}                        |
    |  10. | Kaos Kerah          |  {}                        |
    |  11. | Kaos Rib            |  {}                        |
    |  12. | Kaos Oversize       |  {}                        |
    |  13. | Pashmina            |  {}                        |
    |  14. | Hijab Instan        |  {}                        |
    |  15. | Segiempat           |  {}                        |
    |  16. | Cardigan            |  {}                        |
    |  17. | Jaket Kulit         |  {}                        |
    |  18. | Jaket Parasut       |  {}                        |
    ==========================================================='''.format(
        stok['celana kulot'], stok['celana formal'], stok['celana cargo'],
        stok['kemeja flanel'], stok['kemeja denim'], stok['kemeja linen'],
        stok['rok plisket'], stok['rok a line'], stok['rok span'],
        stok['kaos kerah'], stok['kaos rib'], stok['kaos oversize'],
        stok['pashmina'], stok['hijab instan'], stok['segiempat'],
        stok['cardigan'], stok['jaket kulit'], stok['jaket parasut']
    ))


def hitung_diskon(jumlah):
    diskon = 0

    if jumlah >= 150000:
        diskon += 0.10 
        print("Selamat, Anda Mendapatkan Diskon 10% Karena Belanja Melebihi Rp. 150.000.")

    pilih = input("Apakah Anda Memiliki Kartu Member (y/n) : ")
    if pilih.lower() == 'y':
        diskon += 0.10 
        print("Selamat, Anda Mendapatkan Diskon 10% Karena Memiliki Kartu Member.")

    total_diskon = jumlah - (jumlah * diskon)
    print(f"Total Belanja setelah Diskon: Rp. {int(total_diskon)}")
    return total_diskon

transaksi_harian = [] 

def cetak_struk(pembelian, total_diskon):

    uang = int(input("Uang tunai pembeli: Rp. "))
    kembalian = int(uang - total_diskon) 

    print("\n============================================")
    print("=============== STRUK BELANJA ==============")
    print("============================================")
    import datetime
    saat_ini = datetime.datetime.now()
    print("Tanggal  : ", saat_ini)
    print("Kasir    : ", username)
    print()
    for item in pembelian:
        print(item)
    print(f"Total Belanja: Rp. {int(total_diskon)}")
    print(f"Uang Tunai: Rp. {uang} ")
    print(f"Uang Kembali: Rp. {kembalian}")
    print("===========================================")
    print("===========================================")

    transaksi_harian.append({
        "kasir": username,
        "tanggal": saat_ini,
        "pembelian": pembelian,
        "total": int(total_diskon)
    })

def laporan_harian():
    total_harian = sum(transaksi['total'] for transaksi in transaksi_harian)
    
    print("\n==============================================")
    print("========== LAPORAN PENJUALAN HARIAN ==========")
    print("==============================================")
    print(f"Total Penjualan Hari Ini: Rp. {total_harian}")
    print()
    print("Detail Transaksi:")
    for transaksi in transaksi_harian:
        print(f"Kasir: {transaksi['kasir']}")
        print(f"Tanggal: {transaksi['tanggal']}")
        print("Detail Pembelian:")
        for item in transaksi['pembelian']:
            print(" -", item)
        print(f"Total: Rp. {transaksi['total']}")
        print("===========================================")
    print("=============================================")
    tampilkan_stok()

def menu():
    while True:
        fitur = input('''
      ====== FITUR KASIR ZIGMA SHOP =======
            1. Tambahkan Stok Barang
            2. Tampilkan Semua Stok
            3. Jenis Produk yang Dibeli
            4. Laporan Penjualan Harian
            5. Selesai
                Pilihan Anda: ''')
        
        if fitur == "1":
            tambahkan_stok()
        elif fitur == "2":
            tampilkan_stok()
        elif fitur == "3":
            pembelian, jumlah = jenis_produk()
            if pembelian:
                total_diskon = hitung_diskon(jumlah)
                cetak_struk(pembelian, total_diskon)
            else:
                print("Tidak ada pembelian untuk dicetak.")
        elif fitur == "4":
            laporan_harian()
        elif fitur == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan Anda Salah. Silahkan Pilih Ulang.")

login()
menu()