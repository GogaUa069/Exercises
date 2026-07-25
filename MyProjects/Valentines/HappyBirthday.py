from colorama import Fore, Style


class Cake:
    colors = (Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, "")
    cake = [Fore.LIGHTRED_EX + "      0     0     0" + Style.RESET_ALL,
            "     |v|   |v|   |v|",
            "     | |   | |   | |",
            "   *******************",
            "  {                   }",
            "  {     *         *   }",
            "  {    *         *    }",
            "  {                   }",
            " \\*********************/"]
    happy_birthday = "Happy Birthday to You!"
    person = f"Happy Birthday, dear Egor...."
    congratulations = (happy_birthday, happy_birthday, person, happy_birthday, "")

    def get_congratulations(self):
        for indx in range(len(self.congratulations)):
            print(self.colors[indx] + self.congratulations[indx])

    def get_cake(self):
        for line in self.cake:
            print(line)

    def blow_candles(self):
        input(Fore.LIGHTWHITE_EX + "\n>>> Press ENTER to blow candles\n" + Style.RESET_ALL)
        del self.cake[0]
        self.get_cake()
        print(Fore.LIGHTRED_EX + "\nYey!")


cake = Cake()
cake.get_congratulations()
cake.get_cake()
cake.blow_candles()
