"""
3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.

"""
jelszo = input("Kérem a jelszót!")
helyes_jelszo = "Titok1234#"

while jelszo != helyes_jelszo:
    jelszo = input("Kérem a jelszót!")
else: 
    print("Sikeres belépés!")