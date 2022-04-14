from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, 900, 50))
hunians.append(Rumah("Gustavo Fring", 5, 2, 1500, 150))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 500, 20))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, 1200, 100))

root = Tk()
root.title("Praktikum DPBO Python") # nama programnya

def details(index):
    # nama windownya
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())
    
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # menampilkan datanya
    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    d_pemilik = Label(d_frame, text="Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=1, column=0, sticky="w")
    if(hunians[index].get_jenis() != "Indekos"):
        d_jumlahkamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=2, column=0, sticky="w")
    else:
        d_penghuni = Label(d_frame, text="Penghuni: " + hunians[index].get_nama_penghuni(), anchor="w").grid(row=2, column=0, sticky="w")
    d_listrik = Label(d_frame, text="Kapasitas Listrik: " + hunians[index].get_kapListrik(), anchor="w").grid(row=3, column=0, sticky="w")
    d_luasBangunan = Label(d_frame, text="Luas Tanah: " + hunians[index].get_luasBangunan(), anchor="w").grid(row=4, column=0, sticky="w")
    d_dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=5, column=0, sticky="w")
    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)
    d_exit = Button(opts, text="Exit", command=root.quit)
    d_exit.grid(row=0, column=0)

frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
