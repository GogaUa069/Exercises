import asciichartpy
from secrets import randbelow
from datetime import date, timedelta
from random import choices


class Trading:
    chart_height = 20

    def __init__(self):
        self.today = date.today()
        self.prices = [100]

    def set_new_price(self):
        a, b = randbelow(5000), randbelow(5000)
        new_price = choices([a-b, b-a], weights=[45, 55])[0]
        self.prices.append(new_price)
        if len(self.prices) >= 30:
            del self.prices[0]
        return new_price

    def get_chart(self):
        self.today += timedelta(days=1)
        new_price = self.set_new_price()
        chart = asciichartpy.plot(self.prices, {"height": self.chart_height})
        color = "\033[32m" if self.prices[-1] > self.prices[-2] else "\033[31m"
        print(color + chart + "\033[0m\n")
        print(f"Date: {self.today}")
        print(f"New price: ${new_price}")

    def main_menu(self):
        while True:
            print("\n1. Next day\n2. Quit")
            match input("<<< ").upper():
                case "1" | "NEW DAY":
                    self.get_chart()
                case "2" | "QUIT":
                    break


simulator = Trading()
simulator.main_menu()
