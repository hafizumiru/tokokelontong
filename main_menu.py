import time
import os

def main():
    while True:
        print("\nSelamat datang di L39's Store\n")
        print("Ada yang bisa kami bantu:")
        print("1. Masuk Sebagai Karyawan")
        print("2. Mulai Berbelanja")
        print("0. Keluar Toko")

        pilihan = input("\nMasukkan pilihan Anda: ")

        if pilihan == '1':
            print("Anda memilih Opsi 1.")
        elif pilihan == '2':
            print("Anda memilih Opsi 2.")
        elif pilihan == '0':
            print("Terima kasih atas kunjungannya! Kami tunggu kedatangan Anda kembali.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

        time.sleep(3)
        os.system('cls')

main()
