"""
Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""

szam = int(input("Kérek egy egész számot, és kiszámolom a 1-től a számok összegét: "))
szamolo = 0

for i in range(1, szam+1):
    szamolo += i # alapszam = alapszam + 1
    # print(szamolo)
    print(i)

print(f"A számok 1- től {szam}- ig terjedő összege: {szamolo} ")