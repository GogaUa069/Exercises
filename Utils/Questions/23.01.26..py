from colorama import Fore, Style
import asciichartpy as ac

colors = (Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.CYAN, Fore.MAGENTA)


class Question:
    def __init__(self, question: str, answers: dict):
        self.question = question
        self.answers = answers


q1 = Question("Czy jesteś patriotą?", {"tak": 17, "nie": 10, "nie wiem": 4})
q2 = Question("Czy walczyłbyś o swój kraj?", {"tak": 14, "nie": 10, "nie wiem": 7})
q3 = Question("Za kogo byś głosował za 5 lat na wyborach: Nawrocki, Trzaskowski, komuniści, Obama",
              {"Nawrocki": 3, "Trzaskowski": 4, "komuniści": 4, "Obama": 13, "nie wiem": 7})
q4 = Question("Co byś wybrał: McDonald's, Burger King, Kebab King, warzywa czy MANGO?",
              {"McDonald's": 12, "Burger King": 0, "Kebab King": 5, "warzywa": 4, "MANGO": 8, "nie wiem": 2})
q5 = Question("Czy lubisz 'googoogaga'?", {"tak": 11, "nie": 5, "nie wiem": 15})
q6 = Question("Czy lubisz arabów?", {"tak": 11, "nie": 10, "nie wiem": 10})
q7 = Question("Rambo czy Terminator?", {"Rambo": 10, "Terminator": 7, "nie wiem": 14})
q8 = Question("World of Tanks, World of Warships czy Warthunder?",
              {"WoT": 7, "WoW": 0, "Warthunder": 3, "nie wiem": 21})
q9 = Question("67 czy 69?", {"67": 6, "69": 12, "nie wiem": 13})
q10 = Question("'OK, pa' czy 'Nie, cześć'?", {"'OK, pa'": 5, "'Nie, cześć'": 1, "nie wiem": 25})
q11 = Question("6 razy 8 ...", {"...wygra 48": 6, "...48": 6, "...68": 1, "nie wiem": 8})
q12 = Question("'eaeaa' czy 'gadagadigada'?", {"eaeaa": 2, "gadagadigada": 5, "nie wiem": 24})
q13 = Question("Jaki biznes byś wolał: zbieranie kasztanów czy zbieranie żołędzi?",
               {"Kasztany": 10, "Żołędzie": 1, "nie wiem": 20})
q14 = Question("Czy jesteś 'tan'?", {"tak": 3, "nie": 8, "nie wiem": 20})


class Chart:
    def __init__(self, question: Question):
        self.question = question
        self.values = sorted(list(self.question.answers.values()), reverse=True)
        self.keys = sorted(list(self.question.answers.keys()), reverse=True, key=lambda x: self.question.answers[x])
        self.config = {"colors": [ac.lightred, ac.lightyellow, ac.lightgreen, ac.lightblue, ac.cyan, ac.magenta],
                       "min": 0, "max": max(self.values)}
        self.list_values = list()
        self.set_list_values()

    def set_list_values(self):
        for i, value in enumerate(self.values):
            self.list_values.append([j for j in range(value+1)])

    def get_question_and_legend(self):
        print(f"\nPYTANIE: {self.question.question}\n")
        for indx, item in enumerate(self.keys):
            line = colors[indx] + "|" + Style.RESET_ALL
            print(f"{item} - {line} ({self.question.answers[item]})")
        print()

    def get_chart(self):
        print(ac.plot(self.list_values, self.config))

    def __call__(self):
        self.get_question_and_legend()
        self.get_chart()


chart = Chart(...)
chart()
