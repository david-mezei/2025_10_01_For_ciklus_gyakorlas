"""
5. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:

"""
szam = int(input("Kérek egy számot 1-10-ig: "))
szorzo = 1

for i in range(1, 11):
    print(f"{szam} * {i} = {szam * i}")