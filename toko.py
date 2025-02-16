
import math
import time
import os
from tabulate import tabulate

from data_base import item_toko, members

dict = item_toko
keranjang_belanja = {}


class Toko:
    def menu_toko():
        while True:
            os.system('cls')
            print('Daftar Barang di Toko:')
            toko = []
            for index, (key, value) in enumerate(dict.items()):
                harga = str(
                    math.ceil(value['price'] * 0.9)) + " PROMO 10%!" if value.get('promo') == 1 else str(value['price'])
                toko.append([index + 1, value['name'],
                            value['category'], harga, value['stock']])
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
                lihat_item_promo(dict)
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
                            "\nGunakan Angka 0 untuk kembali): "))
                        if index == 0:
                            keranjang = False
                            continue
                    except:
                        print(
                            "Angka yang ada masukan tidak valid. Tolong masukan hanya angka")
            elif pilihan == '5':
                lakukan_pembayaran()
            elif pilihan == '0':
                return False
            else:
                print("Pilihan tidak valid, silakan coba lagi.")

            time.sleep(2)

# MENU 1


def lihat_item_promo(dict):
    promo_items = []
    for index, (key, value) in enumerate(dict.items()):
        if value.get('promo') == 1:
            promo_items.append([index + 1, value['name'],
                                value['category'], value['price'], math.ceil(value['price'] * 0.9), value['stock']])
    if promo_items:
        print(tabulate(promo_items, headers=[
            'No', 'Nama', 'Kategori', 'Harga Sebelum Promo', 'Harga Sesudah Promo', 'Stok'], tablefmt='grid'))
        belanja = True
        while belanja:
            try:
                index = int(input(
                    "\nTertarik Dengan Item Promo? Masukan ke Keranjang dengan memilih Index Barang(Gunakan angka 0 untuk kembali): "))
                if index == 0:
                    belanja = False
                else:
                    jumlah = int(
                        input("\nMasukkan banyak barang yang Anda inginkan: "))
                    masukan_keranjang(index, jumlah)
            except:
                print(
                    "Angka yang ada masukan tidak valid. Tolong masukan hanya angka")
    else:
        print("Tidak ada item dengan promo.")

# MENU 2


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
            harga = item['price'] * \
                0.9 if item.get('promo') == 1 else item['price']

            if item_name in keranjang_belanja:
                keranjang_belanja[item_name]['jumlah'] += jumlah
            else:
                keranjang_belanja[item_name] = {
                    "price": harga,
                    "jumlah": jumlah
                }
            for key, value in item_toko.items():
                if value['name'] == item_name:
                    item_toko[key]['stock'] -= jumlah
            print(f"{jumlah} {item_name} berhasil ditambahkan ke keranjang dengan harga {'promo' if item.get('promo') == 1 else 'normal'}: {harga}.")

# MENU 4


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


# MENU 5


def lakukan_pembayaran():

    if not keranjang_belanja:
        print("Keranjang belanja kosong. Tidak ada yang bisa dibayar.")
        return

    print("Keranjang Belanja Anda:")
    total_harga = 0
    keranjang = []
    for index, (item_name, value) in enumerate(keranjang_belanja.items()):
        total_item = value['price'] * value['jumlah']
        total_harga += int(total_item)
        keranjang.append(
            [index + 1, item_name, value['price'], value['jumlah'], total_item])

    print(tabulate(keranjang, headers=[
          'No', 'Nama Item', 'Harga per Unit', 'Jumlah', 'Total Harga'], tablefmt='grid'))
    print(f"\nTotal Harga yang harus dibayar: Rp {total_harga:.2f}")

    loop_member = True
    while loop_member:
        try:
            member = int(input(
                "Apakah anda seorang Member(Input 1 untuk Ya atau 0 untuk Tidak): "))
            if member == 0:
                harga_akhir(total_harga)
            elif member == 1:
                member_id = int(input("Masukkan ID Member Anda: "))

                if member_id in members:
                    # Jika ID member valid, terapkan diskon berdasarkan member
                    member_data = members[member_id]

                    total_harga *= 0.95
                    print(
                        f"Selamat, {member_data['name']}! Anda mendapatkan diskon tambahan, Anda hanya perlu membayar sebesar {int(total_harga)}")
                    harga_akhir(int(total_harga))
                    loop_member = False
                else:
                    print("ID Member tidak valid. Kembali Ke pilihan sebelumnya.")

            else:
                print(
                    "Angka yang ada masukan tidak valid. Masukan hanya 0 dan 1")
        except:
            print(
                "Tolong masukan hanya angka")

# Melakukan pembayaran


def harga_akhir(total_harga):
    loop_harga = True
    total_harga = math.ceil(total_harga)
    while loop_harga:
        try:
            # Input jumlah uang dalam kelipatan 100000 atau 50000
            jumlah_100k = int(input("Masukkan jumlah lembar uang Rp100000: "))
            jumlah_50k = int(input("Masukkan jumlah lembar uang Rp50000: "))

            # Hitung total uang yang dibayarkan
            total_uang = (jumlah_100k * 100000) + (jumlah_50k * 50000)

            if total_uang >= total_harga:
                kembalian = total_uang - total_harga
                print(
                    f"\nPembayaran berhasil. Total uang dibayarkan: Rp {total_uang:.2f}")
                print(f"Kembalian Anda: Rp {kembalian:.2f}")

                # Menghitung pecahan uang untuk kembalian
                pecahan_kembalian = hitung_pecahan_uang(kembalian)

                # Tampilkan pecahan kembalian
                if kembalian > 0:
                    print("\nKembalian Anda dengan pecahan:")
                    for pecahan, jumlah in pecahan_kembalian.items():
                        print(f"{jumlah} x Rp {pecahan}")
                else:
                    print("Tidak ada kembalian.")

                # Kurangi stok setiap item yang ada di keranjang belanja
                for item_id, jumlah_beli in keranjang_belanja.items():
                    kurangi_stok(item_id, jumlah_beli)

                # Kosongkan keranjang belanja dan kembali ke menu utama
                keranjang_belanja.clear()
                time.sleep(20)
                loop_harga = False
            else:
                kekurangan = total_harga - total_uang
                print(
                    f"Uang yang Anda masukkan kurang Rp {kekurangan:.2f}. Silakan masukkan jumlah yang tepat.")
        except:
            print("Input tidak valid. Masukkan hanya angka yang sesuai.")


def hitung_pecahan_uang(kembalian):
    pecahan_uang = [20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    pecahan_dibutuhkan = {}

    # Menghitung pecahan uang yang diperlukan
    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            jumlah_pecahan = int(kembalian // pecahan)
            pecahan_dibutuhkan[pecahan] = jumlah_pecahan
            kembalian -= jumlah_pecahan * pecahan

    return pecahan_dibutuhkan


def kurangi_stok(item_id, jumlah_beli):
    if item_id in item_toko:
        stok_sekarang = item_toko[item_id]["stock"]
        if stok_sekarang >= jumlah_beli:
            item_toko[item_id]["stock"] -= jumlah_beli
