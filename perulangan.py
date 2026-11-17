for i in range(1, 6):
    print("Perulangan ke-", i)

n = 3
while n > 0:
    print("Hitung mundur:", n)
    n -= 1

for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    print("Ganjil:", i)
