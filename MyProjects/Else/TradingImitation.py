import asciichartpy
from secrets import randbelow
from datetime import date, timedelta
from random import choices

class Trading:
    def __init__(self):
        self.current_date = date.today()
        self.data_list = [100]

    def set_trading(self):
        first_num = randbelow(10000)
        second_num = randbelow(10000)
        new_num = choices([(a:=first_num-second_num), (a:=second_num-first_num)], weights=[45, 55])[0]
        self.data_list.append(new_num)
        if len(self.data_list) >= 30:
            del self.data_list[0]
        return new_num

    def show_trading(self, height=20):
        self.current_date += timedelta(days=1)
        new_price = self.set_trading()
        chart = asciichartpy.plot(self.data_list, {"height": height})

        if self.data_list[-1] > self.data_list[-2]:
            color = "\033[32m"
        else:
            color = "\033[31m"

        print(color + chart + "\033[0m")
        print(f"\nDate: {self.current_date}")
        print("Starting price: $100")
        print(f"The newest price: {f"${new_price}" if new_price >= 0 else f"-${abs(new_price)}"}")
        max_price = max(self.data_list)
        min_price = min(self.data_list)
        print(f"The highest price in last month was: {f"${max_price}" if max_price >= 0 else f"-${abs(max_price)}"}")
        print(f"The lowest price in last month was: {f"${min_price}" if min_price >= 0 else f"-${abs(min_price)}"}")

    def main_menu(self):
        print("Statistics shown for the last 10 days.")

        while True:
            print("\n"
                  "1. Update trading - show the next day.\n"
                  "2. Quit")
            answer = input("<<< ")
            match answer.upper():
                case "1" | "TRADING":
                    self.show_trading()
                case "2" | "QUIT":
                    break


trading = Trading()
trading.main_menu()
