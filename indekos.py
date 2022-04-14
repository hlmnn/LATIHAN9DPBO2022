from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, kap_Listrik, luas_Tanah):
        super().__init__("Indekos", kap_Listrik, luas_Tanah)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.kap_Listrik = kap_Listrik
        self.luas_Tanah = luas_Tanah

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos. kapasitas listrik " + str(self.kap_Listrik) + " W, dengan luas " + str(self.luas_Tanah) + " m2"