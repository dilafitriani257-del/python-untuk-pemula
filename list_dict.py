buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
print(buah, buah[0], len(buah))

siswa = {"nama": "Dila", "umur": 17, "kelas": "XI"}
siswa["hobi"] = "coding"
for kunci, nilai in siswa.items():
    print(kunci, ":", nilai)
