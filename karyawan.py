from data_base import nota_transaksi

class Karyawan:
    def menu_karyawan():
        print("\nRecap Data Penjualan:")
        for waktu, nota in nota_transaksi.items():
            print(f"\nWaktu Transaksi: {waktu}")
            for item in nota["items"]:
                print(
                    f" - {item['nama_barang']}, Jumlah: {item['jumlah']}, Total: Rp {item['jumlah'] * item['harga']}")
            print(f"Total Harga: Rp {nota['total_harga']}")
