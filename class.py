
"""
class Mahasiswa:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
        
    def perkenalan(self):
        print ("Halo nama saya " + self.nama)
        
siswa = Mahasiswa(nama = "Paijo", usia = 20)
print(siswa.perkenalan())
"""



class Hewan:
    def __init__(self, nama_hewan, suara, habitat):
        self.nama = nama_hewan
        self.suara = suara
        self.habitat = habitat
    
    def identity(self):
        print("Hewan ini bernama " + self.nama + " memiliki suara " + self.suara + " dan berhabitat di " + self.habitat)
        
cheetah = Hewan(nama_hewan = "Cheetah", suara = "Meoww", habitat = "Savamna")
print(cheetah.identity())


class Karyawan:
    def __init__(self, nama_karyawan, gaji, posisi):
        self.nama = nama_karyawan
        self.gaji = gaji
        self.posisi = posisi
    
data_karyawan = Karyawan(nama_karyawan = "Mr. Xyz", gaji = 12000000, posisi = "Data Scientist")

show_nama = data_karyawan.nama
show_gaji = data_karyawan.gaji
show_posisi = data_karyawan.posisi

show = f"""Nama {show_nama:>15}
Gaji {show_gaji:>16}
Posisi {show_posisi:>20}"""

print("\n"+7*"="+"DATA_KARYAWAN"+7*"=")
print(show)