def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

def luas_persegi_panjang(p, l):
    return p * l

print(sapa("Dila"))
print(sapa("Ani", "Selamat pagi"))
print("Luas:", luas_persegi_panjang(5, 3))
