
import math
import time
import os
from datetime import datetime
from tabulate import tabulate

from data_base import item_toko, members, nota_transaksi

keranjang_belanja = {}


class Toko:
    def menu_toko():
        while True:
            os.system('cls')
            print('Daftar Barang di Toko:')
            toko = []
            for index, (item_id, item_detail) in enumerate(item_toko.items()):
                harga = str(
                    math.ceil(item_detail['price'] * 0.9)) + " PROMO 10%!" if item_detail.get('promo') == 1 else str(item_detail['price'])
                toko.append([index + 1, item_detail['name'],
                            item_detail['category'], harga, item_detail['stock']])
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
                    # try:
                    index = int(input(
                        "\nMasukan Index Barang yang akan anda beli(Gunakan angka 0 untuk kembali): "))
                    if index == 0:
                        belanja = False
                    else:
                        jumlah = int(
                            input("\nMasukkan banyak barang yang Anda inginkan: "))
                        masukan_keranjang(index, jumlah)
                    # except:
                    #     print(
                    #         "Angka yang ada masukan tidak valid. Tolong masukan hanya angka")

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
    for index, item_detail in enumerate(dict.items()):
        if item_detail.get('promo') == 1:
            promo_items.append([index + 1, item_detail['name'],
                                item_detail['category'], item_detail['price'], math.ceil(item_detail['price'] * 0.9), item_detail['stock']])
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
    item_list = list(item_toko.items())

    if index < 0 or index >= len(item_list):
        print(f"Index {index} tidak valid.")
    else:
        item_id, item = item_list[index-1]
        if jumlah > item['stock']:
            print(
                f"Stok tidak cukup untuk {item['name']}. Stok tersedia: {item['stock']}.")
        else:

            harga = item['price'] * \
                0.9 if item.get('promo') == 1 else item['price']

            # Tambahkan item ke keranjang menggunakan item_id sebagai key
            if item_id in keranjang_belanja:
                keranjang_belanja[item_id]['jumlah'] += jumlah
            else:
                keranjang_belanja[item_id] = {
                    "name": item['name'],
                    "price": harga,
                    "jumlah": jumlah
                }
            item_toko[item_id]['stock'] -= jumlah
            print(
                f"{jumlah} {item['name']} berhasil ditambahkan ke keranjang dengan harga {'promo' if item.get('promo') == 1 else 'normal'}: {harga}.")


# MENU 4


def lihat_keranjang():
    if not keranjang_belanja:
        print("Keranjang belanja kosong.")
    else:
        keranjang = []
        for index, (item_id, item_detail) in enumerate(keranjang_belanja.items()):
            keranjang.append([index+1, item_detail['name'], item_detail['price'],
                             item_detail['jumlah'], item_detail['price'] * item_detail['jumlah']])
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
    for index, (item_id, item_detail) in enumerate(keranjang_belanja.items()):
        total_item = item_detail['price'] * item_detail['jumlah']
        total_harga += int(total_item)
        keranjang.append(
            [index + 1, item_detail['name'], item_detail['price'], item_detail['jumlah'], total_item])

    print(tabulate(keranjang, headers=[
          'No', 'Nama Item', 'Harga per Unit', 'Jumlah', 'Total Harga'], tablefmt='grid'))
    print(f"\nTotal Harga yang harus dibayar: Rp {total_harga:.2f}")

    loop_member = True
    while loop_member:
        # try:
        member = int(input(
            "Apakah anda seorang Member(Input 1 untuk Ya atau 0 untuk Tidak): "))
        if member == 0:
            harga_akhir(total_harga, keranjang_belanja)
            loop_member = False
        elif member == 1:
            member_id = int(input("Masukkan ID Member Anda: "))

            if member_id in members:
                # Jika ID member valid, terapkan diskon berdasarkan member
                member_data = members[member_id]

                total_harga *= 0.95

                print(
                    f"Selamat, {member_data['name']}! Anda mendapatkan diskon tambahan, Anda hanya perlu membayar sebesar {int(total_harga)}")
                harga_akhir(int(total_harga), keranjang_belanja)
                loop_member = False
            else:
                print("ID Member tidak valid. Kembali Ke pilihan sebelumnya.")

        else:
            print(
                "Angka yang ada masukan tidak valid. Masukan hanya 0 dan 1")
        # except:
        #     print(
        #         "Tolong masukan hanya angka")

# Melakukan pembayaran


def harga_akhir(total_harga, keranjang_belanja):
    loop_harga = True
    total_harga = int(math.ceil(total_harga / 100) * 100)
    while loop_harga:
        # try:
        # Input jumlah uang dalam kelipatan 100000 atau 50000
        jumlah_100k = int(input("Masukkan jumlah lembar uang Rp100000: "))
        jumlah_50k = int(input("Masukkan jumlah lembar uang Rp50000: "))

        # Hitung total uang yang dibayarkan
        total_uang = (jumlah_100k * 100000) + (jumlah_50k * 50000)

        if total_uang >= total_harga:
            kembalian = total_uang - total_harga
            print(
                f"\nPembayaran berhasil. Total uang dibayarkan: Rp {total_uang:,}")
            print(f"Kembalian Anda: Rp {kembalian:,}")

            # Menghitung pecahan uang untuk kembalian
            pecahan_kembalian = hitung_pecahan_uang(kembalian)

            # Tampilkan pecahan kembalian
            if kembalian > 0:
                print("\nKembalian Anda dengan pecahan:")
                for pecahan, jumlah in pecahan_kembalian.items():
                    print(f"{jumlah} x Rp {pecahan:,}")
            else:
                print("Tidak ada kembalian.")

            # Kurangi stok setiap item yang ada di keranjang belanja
            for item_id, item_detail in keranjang_belanja.items():
                kurangi_stok(item_id, item_detail['jumlah'])

            # Buat nota belanja
            nota_belanja = {
                "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_harga": total_harga,
                "item_dibeli": {item_id: {  # Menggunakan item_id sebagai key
                    "name": item_toko[item_id]["name"],  # Nama item
                    "jumlah": item_detail["jumlah"],  # Jumlah item yang dibeli
                    "harga": item_toko[item_id]["price"]  # Harga per item
                    # Iterasi melalui keranjang belanja
                } for item_id, item_detail in keranjang_belanja.items()}
            }

            # Simpan nota ke catatan transaksi
            nota_transaksi[nota_belanja["waktu"]] = nota_belanja

            # Kosongkan keranjang belanja
            keranjang_belanja.clear()

            # Tunggu sebentar dan keluar dari loop
            time.sleep(5)
            loop_harga = False
        else:
            kekurangan = total_harga - total_uang
            print(
                f"Uang yang Anda masukkan kurang Rp {kekurangan:,}. Silakan masukkan jumlah yang tepat.")
        # except ValueError:
        #     print("Input tidak valid. Masukkan hanya angka yang sesuai.")


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
