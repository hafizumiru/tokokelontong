import time
from data_base import nota_transaksi


class Karyawan:
    def menu_karyawan():
        print("\nRecap Data Penjualan:")
        for waktu, nota in nota_transaksi.items():
            print(f"\nWaktu Transaksi: {waktu}")
            # Mengakses 'item_dibeli' dari nota transaksi
            for item_id, item in nota["item_dibeli"].items():
                print(
                    f" - {item['name']}, Jumlah: {item['jumlah']}, Total: Rp {item['jumlah'] * item['harga']}")
            print(f"Total Harga: Rp {nota['total_harga']}")
        time.sleep(10)
