import random

def nadal():
    # Заполнение списков случайными данными
    paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
    tundide_arv = [random.randint(1, 8) for _ in range(7)]
    kas_tootas = [random.choice([True, False]) for _ in range(7)]

    while True:
        # Вывод меню
        print("1. Вывести на экран дни недели в столбик (день-часы)")
        print("2. Отобразить день, в который отработано дольше всего часов и меньше всего")
        print("3. Найти сколько человек отработал часов за неделю")
        print("4. Найти посчитать зарплату за неделю, учитывая что в выходные отлачиваем 1,5 тарифа")
        print("5. Свой вариант")
        print("6. Выход")
        choice = int(input("Выберите действие: "))

        if choice == 1:
            # Вывод дней недели с количеством часов
            for i in range(7):
                print(paevad[i], "-", tundide_arv[i], "часов")

        elif choice == 2:
            # Определение дня с максимальным и минимальным количеством часов
            max_index = tundide_arv.index(max(tundide_arv))
            min_index = tundide_arv.index(min(tundide_arv))
            print("День с максимальным количеством часов:", paevad[max_index])
            print("День с минимальным количеством часов:", paevad[min_index])

        elif choice == 3:
            # Подсчет количества отработанных часов за неделю
            total_hours = sum(tundide_arv)
            print("Отработано часов за неделю:", total_hours)

        elif choice == 4:
            # Расчет зарплаты за неделю с учетом выходных дней
            tariif = float(input("Введите тариф: "))
            total_pay = 0
            for i in range(7):
                if kas_tootas[i]:
                    total_pay += tundide_arv[i] * tariif
                else:
                    total_pay += tundide_arv[i] * tariif * 1.5
            print("Зарплата за неделю:", total_pay)

        elif choice == 5:
            # Добавьте свой вариант действия здесь
            print("Выбран свой вариант действия")

        elif choice == 6:
            # Выход из программы
            break

        else:
            # Некорректный ввод
            print("Некорректный ввод, попробробуйте ещё")
