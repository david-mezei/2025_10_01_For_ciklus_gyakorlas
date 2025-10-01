"""
2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket.

"""

a = int(input("Kérem az első számot: "))
b = int(input("Kérem az második számot: "))



if a < b:
    for i in range(a + 1, b):
        print(i)
elif a > b: 
    for q in range(a - 1, b, -1):
        print(q)
