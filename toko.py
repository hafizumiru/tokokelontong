
import time
import os
from tabulate import tabulate

from data_base import item_toko

dict = item_toko
keranjang_belanja = {}


class Toko:
    def menu_toko():
        while True:
            os.system('cls')
            print('Daftar Barang di Toko:')
            toko = []
            for index, (key, value) in enumerate(dict.items()):
                toko.append([index + 1, value['name'],
                            value['category'], value['price'], value['stock']])
            print(tabulate(toko, headers=[
                  'No', 'Nama', 'Kategori', 'Harga', 'Stok'], tablefmt='grid'))

            print("\nAda yang bisa kami bantu:")
            print("1. Lihat Item Promo")
            print("2. Pilih Barang")
            print("3. Cari Barang")
            print("4. Lihat Keranjang")
            print("5. Lakukan Pembayaran")
            print("0. Kembali")

            pilihan = input("\nMasukkan pilihan Anda: ")

            if pilihan == '1':
                print("Anda memilih Opsi 1.")
            elif pilihan == '2':
                belanja = True
                while belanja:
                    try:
                        index = int(input(
                            "\nMasukan Index Barang yang akan anda beli(Gunakan angka 0 untuk kembali): "))
                        if index == 0:
                            belanja = False
                        else:
                            jumlah = int(
                                input("\nMasukkan banyak barang yang Anda inginkan: "))
                            masukan_keranjang(index, jumlah)
                    except:
                        print(
                            "Angka yang ada masukan tidak valid. Tolong masukan hanya angka")

            elif pilihan == '3':
                print("Anda memilih Opsi 3.")
            elif pilihan == '4':
                keranjang = True
                while keranjang:
                    try:
                        os.system('cls')
                        lihat_keranjang()
                        index = int(input(
                            "\nMasukan Index Barang yang akan anda beli(Gunakan angka 0 untuk kembali): "))
                        if index == 0:
                            keranjang = False
                            continue
                    except:
                        print(
                            "Angka yang ada masukan tidak valid. Tolong masukan hanya angka")
            elif pilihan == '5':
                print("Anda memilih Opsi 5.")
            elif pilihan == '0':
                return False
            else:
                print("Pilihan tidak valid, silakan coba lagi.")

            time.sleep(1)


def masukan_keranjang(index, jumlah):
    item_list = list(item_toko.values())

    if index < 0 or index >= len(item_list):
        print(f"Index {index} tidak valid.")
    else:
        item = item_list[index-1]
        if jumlah > item['stock']:
            print(
                f"Stok tidak cukup untuk {item['name']}. Stok tersedia: {item['stock']}.")
        else:
            item_name = item['name']
            if item_name in keranjang_belanja:
                keranjang_belanja[item_name]['jumlah'] += jumlah
            else:
                keranjang_belanja[item_name] = {
                    "price": item['price'],
                    "jumlah": jumlah
                }
            for key, value in item_toko.items():
                if value['name'] == item_name:
                    item_toko[key]['stock'] -= jumlah
            print(f"{jumlah} {item_name} berhasil ditambahkan ke keranjang.")


def lihat_keranjang():
    if not keranjang_belanja:
        print("Keranjang belanja kosong.")
    else:
        keranjang = []
        for index, (item_name, value) in enumerate(keranjang_belanja.items()):
            keranjang.append([index + 1, item_name, value['price'],
                             value['jumlah'], value['price'] * value['jumlah']])
        print(tabulate(keranjang, headers=[
              'No', 'Nama Item', 'Harga per Unit', 'Jumlah', 'Total Harga'], tablefmt='grid'))
