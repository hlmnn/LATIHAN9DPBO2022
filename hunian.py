class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, kap_Listrik=0, luas_Tanah=0):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.kap_Listrik = kap_Listrik
        self.luas_Tanah = luas_Tanah

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_kapListrik(self):
        return str(self.kap_Listrik) + " W"

    def get_luasBangunan(self):
        return str(self.luas_Tanah) + " m2"

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang, kapasitas listrik " + str(self.kap_Listrik) + " W, dengan luas " + str(self.luas_Tanah) + " m2"