from data_base import item_toko
from tabulate import tabulate


def show_item(dict):
    print('Daftar Barang di Toko:')
    toko = []
    for index, (key, value) in enumerate(dict.items()):
        toko.append([index + 1, value['name'], value['category'],
                    value['price'], value['stock']])
    print(tabulate(toko, headers=['No', 'Nama', 'Kategori', 'Harga', 'Stok']))


cart = []


def masuk_keranjang(cart, dict,  target):
    pass


def show_keranjang(cart):
    print(tabulate(cart))


def delete_item(dict, target):
    for index, (key, value) in enumerate(dict.items()):
        if index == (target-1):
            del dict[key]
            return
    print("Index tidak ditemukan.")


show_item(item_toko)
delete_item(item_toko, 2)

show_item(item_toko)
