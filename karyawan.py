import time
import os
import getpass
from tabulate import tabulate
from data_base import nota_transaksi, karyawan


class Karyawan:
    def login():
        while True:
            print("Silahkan masukan Username dan Password")
            username = input("Masukkan username: ")
            # Menggunakan getpass untuk menyembunyikan input password
            password = getpass.getpass("Masukkan password: ")

            # Verifikasi login
            if verifikasi_login(username, password):
                masuk_menu(username)
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
            pass
        elif pilihan == '2':
            pass

        elif pilihan == '3':
            recap_penjualan(nota_transaksi)
        elif pilihan == '0':
            return False
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


def recap_penjualan(nota_transaksi):
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

    # Siapkan data untuk ditampilkan dalam tabel
    tabel_data = []
    for item in rekap_penjualan_item.values():
        tabel_data.append([item['name'], item['jumlah'], item['total_harga']])

    # Menampilkan tabel dengan tabulate
    print(tabulate(tabel_data, headers=[
          "Nama Barang", "Jumlah Terjual", "Total Harga"], tablefmt="grid"))

    # Menampilkan total harga keseluruhan dari semua nota
    print(f"\nTotal Semua Nota: Rp {total_semua_nota}")
    time.sleep(10)
