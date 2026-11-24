class Pesanan:

    # Atribut
    def __init__(self):
        self.__id_pesanan = None
        self.__pelanggan = None
        self.__meja = None
        self.__detail_pesanan = None     
        self.__pembayaran = None
        self.__status = None

    # Method
    def _pastikan_belum_lunas(self):
        pass

    def _cari_detail(self, menu):
        pass

    def tambah_item(self, menu, jumlah):
        pass

    def hapus_item(self, menu):
        pass

    def hitung_subtotal(self):
        pass

    def hitung_total(self):
        pass

    def bayar(self, pembayaran, nominal=None):
        pass

    def cetak_struk(self):
        pass
