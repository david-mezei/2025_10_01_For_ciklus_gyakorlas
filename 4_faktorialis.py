# 1. feladat megoldása átdolgozva

szam = int(input("Kérek egy egész számot, és kiszámolom a faktoriálisát: "))
fakt = 1

for i in range(1, szam + 1):
    fakt *= i

print(f"{szam} faktoriálisa {fakt}")