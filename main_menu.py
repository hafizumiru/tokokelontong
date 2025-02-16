import time
import os

from toko import Toko
from karyawan import Karyawan

toko = Toko
karyawan = Karyawan

def main():

    while True:
        os.system('cls')
        print("\nSelamat datang di L39's Store\n")
        print("1. Masuk Sebagai Karyawan")
        print("2. Mulai Berbelanja")
        print("0. Keluar Toko")

        pilihan = input("\nMasukkan pilihan Anda: ")

        if pilihan == '1':
            karyawan.menu_karyawan()
        elif pilihan == '2':
            toko.menu_toko()
        elif pilihan == '0':
            os.system('cls')
            print("Terima kasih atas kunjungannya! Kami tunggu kedatangan Anda kembali.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


main()
