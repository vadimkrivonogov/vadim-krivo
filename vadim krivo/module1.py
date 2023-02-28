import random

paevad = ['E', 'T', 'K', 'N', 'R', 'L', 'P']
tundide_arv = [random.randint(1, 10) for _ in range(7)]
nadalalopul = [random.choice([True, False]) for _ in range(7)]

while True:
    print("Vali tegevus:")
    print("1. Kuva töötatud tunnid päevade kaupa")
    print("2. Leia päev, mil töötati kõige rohkem ja kõige vähem tunde")
    print("3. Leia kokku töötatud tunnid nädala jooksul")
    print("4. Arvuta nädalapalk")
    print("5. Enda versioon")
    print("0. Lõpeta programmi töö")
    valik = input("Sisesta valik (0-5): ")

    if valik == "0":
        break
    elif valik == "1":
        for i, paev in enumerate(paevad):
            print(f"{paev}: {tundide_arv[i]}")
    elif valik == "2":
        maksimum = tundide_arv.index(max(tundide_arv))
        miinimum = tundide_arv.index(min(tundide_arv))
        print(f"Kõige rohkem töötati tunde ({tundide_arv[maksimum]}) päeval {paevad[maksimum]}")
        print(f"Kõige vähem töötati tunde ({tundide_arv[miinimum]}) päeval {paevad[miinimum]}")
    elif valik == "3":
        kokku = sum(tundide_arv)
        print(f"Kokku töötatud tunnid: {kokku}")
    elif valik == "4":
        tunnitasu = float(input("Sisesta tunnitasu: "))
        kokku = 0
        for i, paev in enumerate(paevad):
            if nadalalopul[i]:
                kokku += tundide_arv[i] * 1.5 * tunnitasu
            else:
                kokku += tundide_arv[i] * tunnitasu
        print(f"Nädalapalk: {kokku}")
    elif valik == "5":
        # Siia saad lisada oma versiooni
        print("Enda versioon pole veel rakendatud")
    else:
        print("Vigane valik")
