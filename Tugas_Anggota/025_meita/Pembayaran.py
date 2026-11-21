from abc import ABC, abstractmethod


class Pembayaran(ABC):

    # Atribut
    def __init__(self):
        self.__id_bayar = None
        self.__total = None
        self.__status = None

    # Method
    @abstractmethod
    def proses_bayar(self, nominal):
        pass

    def info(self):
        pass


class PembayaranTunai(Pembayaran):

    # Atribut
    def __init__(self):
        super().__init__()
        self.__uang_diterima = None

    # Method
    def proses_bayar(self, nominal):
        pass

    def hitung_kembalian(self):
        pass

    def info(self):
        pass


class PembayaranQRIS(Pembayaran):

    # Atribut
    def __init__(self):
        super().__init__()
        self.__kode_qr = None
        self.__provider = None

    # Method
    def proses_bayar(self, nominal):
        pass

    def info(self):
        pass


class PembayaranDebit(Pembayaran):

    # Atribut
    def __init__(self):
        super().__init__()
        self.__nomor_kartu = None
        self.__bank = None

    # Method
    def proses_bayar(self, nominal):
        pass

    def info(self):
        pass