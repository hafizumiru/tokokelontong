import time
import os
import pwinput

from tabulate import tabulate

from data_base import nota_transaksi, karyawan, item_toko, members


class Karyawan:
    def login():
        while True:
            print("Silahkan masukan Username dan Password")
            username = input("Masukkan username: ")
            # Menggunakan getpass untuk menyembunyikan input password
            password = pwinput.pwinput("Masukkan password: ")

            # Verifikasi login
            if verifikasi_login(username, password):
                masuk_menu(username)
                return False
            else:
                print("Login gagal! Username atau password salah.")


def verifikasi_login(username, password):
    for user in karyawan:
        if user["username"] == username and user["password"] == password:
            return True
    return False


def masuk_menu(username):
    while True:
        os.system('cls')
        print(f"\nSelamat datang {username}:")
        print("1. Lihat Item Toko")
        print("2. Lihat Daftar Member")
        print("3. Lihat Total Penjualan")
        print("0. Logout")

        pilihan = input("\nMasukkan pilihan Anda: ")

        if pilihan == '1':
            lihat_item(item_toko)
        elif pilihan == '2':
            lihat_member(members)
        elif pilihan == '3':
            recap_penjualan(nota_transaksi)
        elif pilihan == '0':
            return False
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Fungsi Daftar Item


def lihat_item(item_toko):
    while True:
        os.system('cls')
        print('Daftar Barang di Toko:')
        toko = []
        for index, (item_id, item_detail) in enumerate(item_toko.items()):
            if not item_detail['is_deleted']:
                toko.append([item_id, item_detail['name'],
                             item_detail['category'], item_detail['price'], item_detail['stock']])
        print(tabulate(toko, headers=[
            'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))

        print(f"\nPilih Menu")
        print("1. Tambah Item Toko")
        print("2. Hapus Item Toko")
        print("3. Tambah Stock Item")
        print("4. Edit Promo")
        print("5. Restore Item yang Terhapus")
        print("0. Back")

        pilihan = input("\nMasukkan pilihan Anda: ")

        if pilihan == '1':
            tambah_item(item_toko)
        elif pilihan == '2':
            hapus_item(item_toko)
        elif pilihan == '3':
            tambah_stok(item_toko)
        elif pilihan == '4':
            edit_promo(item_toko)
        elif pilihan == '5':
            restore_item(item_toko)
        elif pilihan == '0':
            return False
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


def tambah_item(item_toko):
    os.system('cls')
    print("Tambah Item Toko")

    if len(item_toko) == 0:
        kode_item_baru = "item_001"
    else:
        # Proses Auto Increment
        kode_item_terakhir = sorted(item_toko.keys())[-1]
        nomor_terakhir = int(kode_item_terakhir.split('_')[1])
        kode_item_baru = f"item_{str(nomor_terakhir + 1).zfill(3)}"

    nama = input("Masukkan Nama Item: ")
    kategori = input("Masukkan Kategori (1 untuk Food, 2 untuk Household): ")
    while True:
        if kategori == "1":
            kategori = "Food"
            break
        elif kategori == "2":
            kategori == "Household"
            break
        else:
            print("Masukan Angka sesuai Perintah")

    harga = float(input("Masukkan Harga: "))
    stok = int(input("Masukkan Jumlah Stok: "))

    # Menambahkan item ke dalam dictionary
    item_toko[kode_item_baru] = {
        "name": nama,
        "category": kategori,
        "price": harga,
        "stock": stok,
        "is_promo": 0,
        "is_deleted": 0
    }
    print(f"Item {nama} berhasil ditambahkan dengan kode {kode_item_baru}.")
    time.sleep(3)
    return item_toko


def hapus_item(item_toko):
    print('Daftar Barang di Toko:')
    toko = []
    for index, (item_id, item_detail) in enumerate(item_toko.items()):
        if not item_detail['is_deleted']:
            toko.append([item_id, item_detail['name'],
                        item_detail['category'], item_detail['price'], item_detail['stock']])
    print(tabulate(toko, headers=[
        'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))
    id_hapus = input("Masukan ID barang yang akan dihapus: ")
    if id_hapus in item_toko:
        item_toko[id_hapus]['is_deleted'] = 1
        print(f"Item {id_hapus} berhasil dihapus")
        time.sleep(5)
    else:
        print(f"Item {item_id} tidak ditemukan.")


def tambah_stok(item_toko):
    os.system('cls')
    print("Tambah Stok Item")
    toko = []
    for index, (item_id, item_detail) in enumerate(item_toko.items()):
        if not item_detail['is_deleted']:
            toko.append([item_id, item_detail['name'],
                         item_detail['category'], item_detail['price'], item_detail['stock']])
    print(tabulate(toko, headers=[
        'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))
    kode_item = input(
        "\nMasukkan Kode Item yang ingin ditambah stoknya: ")
    if kode_item in item_toko:
        stok_baru = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
        item_toko[kode_item]['stock'] += stok_baru
        print(f"Stok item {item_toko[kode_item]['name']} berhasil diperbarui.")
    else:
        print(f"Item dengan kode {kode_item} tidak ditemukan.")
    return item_toko


def edit_promo(item_toko):
    while True:
        os.system("cls")
        print('Daftar Barang Promo:')
        promo = []
        for index, (item_id, item_detail) in enumerate(item_toko.items()):
            if item_detail['is_promo']:
                promo.append([item_id, item_detail['name'],
                              item_detail['category'], item_detail['price'], item_detail['stock']])
        print(tabulate(promo, headers=[
            'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))
        print('Daftar Barang Non-Promo:')
        non_promo = []
        for index, (item_id, item_detail) in enumerate(item_toko.items()):
            if not item_detail['is_promo']:
                non_promo.append([item_id, item_detail['name'],
                                  item_detail['category'], item_detail['price'], item_detail['stock']])
        print(tabulate(non_promo, headers=[
            'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))

        ganti_promo = input(
            "Masukan ID barang yang akan diganti promo:(Ketik 0 untuk kembali) ")

        if ganti_promo == "0":
            break
        elif ganti_promo in item_toko:
            item_toko[ganti_promo]['is_promo'] = 0 if item_toko[ganti_promo]['is_promo'] == 1 else 1
            print(f"Promo pada Item {ganti_promo} berhasil diganti")
            time.sleep(2)
        else:
            print(f"Item {item_id} tidak ditemukan. Masukan ID yang tepat")


def restore_item(item_toko):
    print('Daftar Barang di Toko:')
    toko = []
    for index, (item_id, item_detail) in enumerate(item_toko.items()):
        if item_detail['is_deleted']:
            toko.append([item_id, item_detail['name'],
                        item_detail['category'], item_detail['price'], item_detail['stock']])
    print(tabulate(toko, headers=[
        'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))
    id_restore = input("Masukan ID barang yang akan direstore: ")
    if id_restore in item_toko:
        item_toko[id_restore]['is_deleted'] = 0
        print(f"Item {id_restore} berhasil direstore")
        time.sleep(5)
    else:
        print(f"Item {item_id} tidak ditemukan.")

# Fungsi Daftar Member


def lihat_member(members):
    # while True:
    #     os.system('cls')
    #     print('Daftar Barang di Toko:')
    #     toko = []
    #     for index, (item_id, item_detail) in enumerate(item_toko.items()):
    #         toko.append([index + 1, item_id, item_detail['name'],
    #                     item_detail['category'], item_detail['price'], item_detail['stock']])
    #     print(tabulate(toko, headers=[
    #           'No', 'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))

    #     print(f"\nPilih Menu")
    #     print("1. Tambah Item Toko")
    #     print("2. Hapus Item Toko")
    #     print("3. Tambah Stock Item")
    #     print("4. Edit Promo")
    #     print("5. Restore Item yang Terhapus")
    #     print("0. Back")

    #     pilihan = input("\nMasukkan pilihan Anda: ")

    #     if pilihan == '1':
    #         print("1")
    #     elif pilihan == '2':
    #         print("2")
    #     elif pilihan == '3':
    #         print("3")
    #     elif pilihan == '4':
    #         print("3")
    #     elif pilihan == '5':
    #         print("3")
    #     elif pilihan == '0':
    #         return False
    #     else:
    #         print("Pilihan tidak valid, silakan coba lagi.")
    pass

# Fungsi Recap Penjualan


def recap_penjualan(nota_transaksi):
    fungsi_recap = True
    while fungsi_recap:
        print("\nRecap Data Penjualan:")

        # Dictionary untuk merekap jumlah penjualan item dari semua transaksi
        rekap_penjualan_item = {}
        total_semua_nota = 0

        # Looping setiap transaksi
        for waktu, nota in nota_transaksi.items():
            total_semua_nota += nota['total_harga']
            for item_id, item in nota["item_dibeli"].items():
                if item_id not in rekap_penjualan_item:
                    rekap_penjualan_item[item_id] = {
                        "name": item['name'],
                        "jumlah": item['jumlah'],
                        "total_harga": item['jumlah'] * item['harga']
                    }
                else:
                    rekap_penjualan_item[item_id]["jumlah"] += item['jumlah']
                    rekap_penjualan_item[item_id]["total_harga"] += item['jumlah'] * item['harga']

        tabel_data = []
        for item in rekap_penjualan_item.values():
            tabel_data.append(
                [item['name'], item['jumlah'], item['total_harga']])

        print(tabulate(tabel_data, headers=[
            "Nama Barang", "Jumlah Terjual", "Total Harga"], tablefmt="grid"))

        print(f"\nTotal Semua Nota: Rp {total_semua_nota}")

        index = input("\nGunakan Angka 0 untuk kembali): ")
        if index == "0":
            break
