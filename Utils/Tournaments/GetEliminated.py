from prettytable import PrettyTable

players = [
    {"fio": "Yehor Pavlenko 8A", "time": 12.46},
    {"fio": "Seweryn Kuligowski 8A", "time": 16.16},
    {"fio": "Martyna Chodera 8A", "time": 14.78},
    {"fio": "Emilia Główczewska 8A", "time": 12.47},
    {"fio": "Maja Lewandowska 8D", "time": 13.26},
    {"fio": "Nikola Krawczek 8D", "time": 18.28},
    {"fio": "Ola Winiecka 8D", "time": 14.48},
    {"fio": "Tomasz Krajewski 7A", "time": 25.90},
]

players.sort(key=lambda x: x["time"], reverse=True)
elimination_counter = len(players) // 2

eliminated_players = players[:elimination_counter]
passed_players = players[elimination_counter:]

border = PrettyTable()
border.field_names = ["PRZESZLI DALEJ", "WYELIMINOWANI"]

for pair in zip(passed_players, eliminated_players):
    border.add_row([pl["fio"] for pl in pair])

print(border, end="\n")
