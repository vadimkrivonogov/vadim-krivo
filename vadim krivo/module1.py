import random

paevad = ['E', 'T', 'K', 'N', 'R', 'L', 'P']
tundide_arv = [random.randint(1, 10) for _ in range(7)]
nadalalopul = [random.choice([True, False]) for _ in range(7)]

while True:
    print("Vali tegevus:")
    print("1. Kuva t��tatud tunnid p�evade kaupa")
    print("2. Leia p�ev, mil t��tati k�ige rohkem ja k�ige v�hem tunde")
    print("3. Leia kokku t��tatud tunnid n�dala jooksul")
    print("4. Arvuta n�dalapalk")
    print("5. Enda versioon")
    print("0. L�peta programmi t��")
    valik = input("Sisesta valik (0-5): ")

    if valik == "0":
        break
    elif valik == "1":
        for i, paev in enumerate(paevad):
            print(f"{paev}: {tundide_arv[i]}")
    elif valik == "2":
        maksimum = tundide_arv.index(max(tundide_arv))
        miinimum = tundide_arv.index(min(tundide_arv))
        print(f"K�ige rohkem t��tati tunde ({tundide_arv[maksimum]}) p�eval {paevad[maksimum]}")
        print(f"K�ige v�hem t��tati tunde ({tundide_arv[miinimum]}) p�eval {paevad[miinimum]}")
    elif valik == "3":
        kokku = sum(tundide_arv)
        print(f"Kokku t��tatud tunnid: {kokku}")
    elif valik == "4":
        tunnitasu = float(input("Sisesta tunnitasu: "))
        kokku = 0
        for i, paev in enumerate(paevad):
            if nadalalopul[i]:
                kokku += tundide_arv[i] * 1.5 * tunnitasu
            else:
                kokku += tundide_arv[i] * tunnitasu
        print(f"N�dalapalk: {kokku}")
    elif valik == "5":
        # Siia saad lisada oma versiooni
        print("Enda versioon pole veel rakendatud")
    else:
        print("Vigane valik")
