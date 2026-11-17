class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Saya {self.nama}, kelas {self.kelas}"

s1 = Siswa("Dila", "XI")
s2 = Siswa("Ani", "XII")
print(s1.perkenalan())
print(s2.perkenalan())
