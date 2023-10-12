import math
print("16.feladat")
# Oldalak beolvasása a konzolról
a = float(input("Adja meg a háromszög oldalhosszát: "))

# Hibakezelés: Ellenőrizze, hogy az oldal pozitív-e
if a <= 0:
    print("Hiba: a háromszög oldala nem pozitív!")
else:
    # Számítsa ki a kerületet és a területet
    kerulet = 3 * a
    terulet = (math.sqrt(3) / 4) * (a ** 2)

    # Kiírja az eredményeket
    print(f"A háromszög kerülete: {kerulet}")
    print(f"A háromszög területe: {terulet}")

print("12.feladat")
szam1 = float(input("Kérem adja meg az első számot: "))
szam2 = float(input("Kérem adja meg a második számot: "))

# Számok összehasonlítása és a relációs jel kiírása
if szam1 < szam2:
    print(f"{szam1} < {szam2}")
elif szam1 > szam2:
    print(f"{szam1} > {szam2}")
else:
    print(f"{szam1} = {szam2}")
print("13.feladat")
import math

# Kör sugara beolvasása a konzolról
sugar = float(input("Kérem adja meg a kör sugarát: "))

# Hibakezelés: Ellenőrizze, hogy a sugár pozitív-e
if sugar <= 0:
    print("Hiba: a kör sugara nem pozitív!")
else:
    # Számítsa ki a kerületet és a területet
    kerulet = 2 * math.pi * sugar
    terulet = math.pi * sugar ** 2

    # Kiírja az eredményeket
    print(f"A kör kerülete: {kerulet}")
    print(f"A kör területe: {terulet}")

