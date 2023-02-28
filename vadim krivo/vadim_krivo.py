import random

def nadal():
    paevad = ['E', 'T', 'K', 'N', 'R', 'L', 'P']
    tundide_arv = [random.randint(1, 10) for _ in range(7)]
    on_weekends = [random.choice([True, False]) for _ in range(7)]
    return paevad, tundide_arv, on_weekends

def kuva_tundide_arv(paevad, tundide_arv):
    for i, paev in enumerate(paevad):
        print(f"{paev}: {tundide_arv[i]}")

def leia_max_min_tunnid(paevad, tundide_arv):
    max_index = tundide_arv.index(max(tundide_arv))
    min_index = tundide_arv.index(min(tundide_arv))
    print(f"Maksimaalsed tunnid ({tundide_arv[max_index]}) on päeval {paevad[max_index]}")
    print(f"Minimaalsed tunnid ({tundide_arv[min_index]}) on päeval {paevad[min_index]}")

def kokku_tunnid(tundide_arv):
    return sum(tundide_arv)

def arvuta_palk(paevad, tundide_arv, on_weekends, tariff):
    total = 0
    for i, paev in enumerate(paevad):
        if on_weekends[i]:
            total += tundide_arv[i] * 1.5 * tariff
        else:
            total += tundide_arv[i] * tariff
    return total

def enda_versioon(paevad, tundide_arv, on_weekends):
    # Sinu enda versioon tuleb siia
    print("Enda versioon pole veel implementeeritud")

paevad, tundide_arv, on_weekends = nadal()

while True:
    print("Vali tegevus:")
    print("1. Kuva päeva töötunnid")
    print("2. Leia päev, kus töötati kõige rohkem ja vähem")
    print("3. Leia nädala töötundide kogusumma")
    print("4. Arvuta palk nädala eest")
    print("5. Enda versioon")
    print("0. Välju")
    choice = input("Sisesta oma valik (0-5): ")

    if choice == "0":
        break
    elif choice == "1":
        kuva_tundide_arv(paevad, tundide_arv)
    elif choice == "2":
        leia_max_min_tunnid(paevad, tundide_arv)
    elif choice == "3":
        total = kokku_tunnid(tundide_arv)
        print(f"Nädala töötunnid kokku: {total}")
    elif choice == "4":
        tariff = float(input("Sisesta tunnitasu: "))
        salary = arvuta_palk(paevad, tundide_arv, on_weekends, tariff)
        print(f"Palk nädala eest: {salary}")
    elif choice == "5":
        enda_versioon(paevad, tundide_arv, on_weekends)
    else:
        print("Vigane valik")
