name_list = ["Aleksandra", "Alicja", "Filip", "Maks", "Martyna", "Mikołaj", "Rafał", "Sambor", "Wiktor", "Bogdan",
             "Denis", "Wiśnia"]

sorted_names = sorted(name_list)


def get_names():
    counter = 1
    for name in sorted_names:
        print(f"{counter}. {name}")
        counter += 1
