from abc import ABC, abstractmethod


class Menu(ABC):
    # Class induk (abstract) untuk semua item menu.

    def __init__(self, id_menu, nama, harga, stok):
        self.__id_menu = None
        self.__nama = None
        self.__harga = None
        self.__stok = None

    @property
    def id_menu(self):
        pass

    @property
    def nama(self):
        pass

    @property
    def harga(self):
        pass

    @property
    def stok(self):
        pass

    def cek_stok(self, jumlah):
        pass

    def kurangi_stok(self, jumlah):
        pass

    def tambah_stok(self, jumlah):
        pass

    @abstractmethod
    def hitung_harga(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Makanan(Menu):
    # Menu makanan dengan tingkat pedas.

    def __init__(self, id_menu, nama, harga, stok, tingkat_pedas=0):
        super().__init__(id_menu, nama, harga, stok)
        self.__tingkat_pedas = None

    @property
    def tingkat_pedas(self):
        pass

    def hitung_harga(self):
        pass

    def info(self):
        pass


class Minuman(Menu):
    # Menu minuman dengan ukuran dan suhu.

    def __init__(self, id_menu, nama, harga, stok, ukuran="M", dingin=False):
        super().__init__(id_menu, nama, harga, stok)
        self.__ukuran = None
        self.__dingin = None

    @property
    def ukuran(self):
        pass

    @property
    def dingin(self):
        pass

    def hitung_harga(self):
        pass

    def info(self):
        pass