import time
import os
import pwinput

from tabulate import tabulate

from data_base import nota_transaksi, karyawan, item_toko


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
            pass
        elif pilihan == '3':
            recap_penjualan(nota_transaksi)
        elif pilihan == '0':
            return False
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


def lihat_item(item_toko):
    while True:
        os.system('cls')
        print('Daftar Barang di Toko:')
        toko = []
        for index, (item_id, item_detail) in enumerate(item_toko.items()):
            toko.append([index + 1, item_id, item_detail['name'],
                        item_detail['category'], item_detail['price'], item_detail['stock']])
        print(tabulate(toko, headers=[
              'No', 'Kode Item', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))

        print(f"\nPilih Menu")
        print("1. Tambah Item Toko")
        print("2. Hapus Item Toko")
        print("3. Tambah Stock Item")
        print("0. Back")

        pilihan = input("\nMasukkan pilihan Anda: ")

        if pilihan == '1':
            print("1")
        elif pilihan == '2':
            print("2")
        elif pilihan == '3':
            print("3")
        elif pilihan == '0':
            return False
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


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

        index = int(input(
            "\nGunakan Angka 0 untuk kembali): "))
        if index == 0:
            fungsi_recap = False
            continue
