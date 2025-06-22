from time import sleep
from colorama import Fore, Style
from random import shuffle, choice

groceries = {"das Brot": "chleb", "die Brezel": "precel", "das Brötchen": "bułka", "die Butter": "masło",
             "die Cornflakes": "płatki kukurydziane", "das Croissant": "rogal", "das Ei": "jajo",
             "das Fleisch": "mięso", "der Fisch": "ryba", "der Hönig": "miód", "der/das Joghurt": "jogurt",
             "der/das Fruchtjoghurt": "jogurt owocowy", "der Käse": "ser żółty", "der/das Ketchup": "keczup",
             "die Marmelade": "marmolada", "der Quark": "twaróg", "der Reis": "ryż", "das Salz": "sól",
             "der Schinken": "szynka", "die Schokolade": "czekolada", "der Schokoriegel": "baton czekoladowy",
             "das Schwarzbrot": "czarny chleb", "der Thunfisch": "tuńczyk", "die Wurst": "kiełbasa"}

plants = {"der Apfel": "jabłko", "das Gemüse": "warzywa", "die Grapefruit": "grejpfrut", "die Gurke": "ogórek",
          "das Obst": "owoce", "die Orange": "pomarańcza", "der Salat": "sałata", "die Tomate": "pomidor",
          "die Zitrone": "cytryna", "die Zwiebel": "cebula"}

drinks = {"der Apfelsaft": "sok jabłkowy", "das Getränk": "napój",
          "die Getränke": "napoje", "heisse Schokolade": "gorąca czekolada", "der Kaffee": "kawa",
          "der Kakao": "kakao", "die Limonade": "lemoniada", "die Milch": "mleko",
          "das Mineralwasser": "woda mineralna", "der Saft": "sok", "ein Glas Saft": "szklanka soku",
          "der Tee": "herbata", "der Eistee": "herbata mrożona", "der Früchtetee": "herbata owocowa",
          "Tee mit Zitrone": "herbata z cytryną", "eine Dose Limonade": "puszka lemoniady"}

food = {"die Bratkartoffeln": "smażone ziemniaki", "die Brühe": "rosół", "die Currywurst": "kiełbasa z curry",
        "der Käse-Schinken-Toast": "tost z szynką i serem", "die Nudel": "kluska", "die Nudeln": "kluski",
        "die Pizza": "pizza", "die Pommes frites": "frytki", "die Schwarzbohnen": "czarna fasola",
        "ein Stück Pizza": "kawałek pizzy", "die Sosse": "sos", "die Suppe": "zupa",
        "die Tomatensuppe": "pomidorówka", "die Gemüsesalat": "sałatka warzywna"}

taste_and_appearance_of_food = {"fett": "tłusty", "gesund": "zdrowy", "ungesund": "niezdrowy", "gut": "dobry",
                                "schlecht": "zły", "schmecken": "smakować", "das Schulessen": "jedzenie szkolne",
                                "Wie schmeckt das Schulessen?": "jak smakuje w jedzenie w szkole?",
                                "Das Schulessen schmeckt gut": "jedzenie w szkole smakuje dobrze",
                                "Ich finde das Schulessen gesund": "Sądzę, że jedzenie w szkole jest zdrowe."}

regional_dishes = {"der Apfelstrudel": "sztrudel z jabłkami", "die Bratwurst": "kiełbasa pieczona",
                   "der Eintopf": "potrawa jednogarnkowa", "das Fondue": "fondue", "die Rösti": "placek ziemniaczany",
                   "die Sachertorte": "tort czekoladowy",
                   "die Schweinshaxe mit Sauerkraut": "golonka z kiszoną kapustą",
                   "das Wiener Schnitzel": "sznycel po wiedeńsku", "zubereiten": "przyrządzać",
                   "Die Rösti bereitet man aus Kartoffeln zu": "placek ziemniaczany przyrządza się z ziemniaków"}

gastronomic_locals = {"amüsieren, sich": "bawić się", "befinden, sich": "znajdować się", "die Cafeteria": "kafejka",
                      "in der Cafeteria": "w kafejce", "ernähren, sich": "odżywiać się",
                      "die Imbissbude": "budka z jedzeniem", "an einer Imbissbude": "przy budce z jedzeniem",
                      "vor einer Imbissbude": "przed budką z jedzeniem", "der Junge": "chłopiec",
                      "die Jungen": "chłopcy", "die Jungs": "chłopcy (wersja potoczna)",
                      "das Lieblingsessen": "ulubione danie", "das Mädchen": "dziewczyna", "die Mädchen": "dziewczyny",
                      "die Salatbar": "bar sałatkowy", "in einer Salatbar": "w barze sałatkowym",
                      "die Schulcafeteria": "stołówka szkolna", "verabreden, sich": "umawiać się",
                      "Ich habe Hunger": "jestem głodny 1", "Ich bin hungrig": "jestem głodny 2",
                      "Ich habe Durst": "jestem spragniony 1", "Ich bin durstig": "jestem spragniony 2"}

expressions = {"im Geschäft": "w sklepie", "im Restaurant": "w restauracji", "der Gast": "gość", "die Gäste": "goście",
               "die Rechnung": "rachunek", "die Speisekarte": "menu", "der Nachtisch": "deser",
               "zum Nachtisch": "na deser", "die Packung": "pudełko", "das Souvenir": "pamiątka",
               "die Souvenirs": "pamiątki", "Souvenirs aus Wien": "pamiątki z Wiednia", "die Tafel": "tabliczka",
               "eine Tafel Schokolade": "tabliczka czekolady", "die Verkäuferin": "ekspedientka",
               "Was kostet die Schokolade?": "Ile kosztuje czekolada?",
               "Die Schokolade kostet 1,20 Euro": "czekolada kosztuje 1,20 Euro",
               "Das macht zusammen 6,30 Euro": "To wynosi razem 6,30 Euro", "70 Cent zurück": "70 centów reszty",
               "Bitte sehr": "proszę bardzo", "Bitte, hier ist die Speisekarte": "Proszę, tutaj jest karta dań",
               "Nehmen Sie bitte Platz!": "Proszę zająć miejsce", "Was möchten Sie?": "Co sobie państwo życzą? 1",
               "Sie wünschen?": "Co sobie państwo życzą? 2", "Ich möcte eine Brühe": "Chciałbym rosół 1",
               "Eine Brühe, bitte": "Chciałbym rosół 2", "Sonst noch etwas?": "Czy coś jeszcze? 1",
               "Nehmen Sie noch etwas?": "czy coś jeszcze? 2", "Kommt sofort": "natychmiast",
               "Nein, danke. Das ist alles": "Nie, dziękuję. To wszystko"}

man = ("\nZaimek nieosobowy 'man' występuje w zdaniu w roli podmiotu, jeśli wykonawca nie jest określony.\n"
       "Man łączy się z czasownikiem 3 os.l.p.; np. Man trinkt hier Kaffee. - Tutaj PIJE SIĘ kawę.")

mochte_form = ("\nForma möchte... oznacza CHCIAŁBYM.\n"
               "Może występować w dwoch formach, np.:\n"
               "1. Ich möchte eine Limonade.\n"
               "2. Er möchte Saft trinken.")

verbs = ("\nZaimek zwrotny 'sich'. W języku polskim - się.\n"
         "Sich występuje blisko orzeczenia.\n"
         "Uwaga! Nie wszystkie czasowniki zwrotne w j.polskim są zwrotne w j.niemieckim i odwrotnie.")

imperative = ("\nTryb rozkazujący tworzy się dla 2os.l.p.; 1 i 2os.l.mn. oraz dla formy grzecznościowej.\n"
              "Tworzenie trybu rozkazującego dla poszczególnych osób:\n"
              "Du - odrzuca zaimek osobowy i końcówkę -st, dodaj -e (jak trzeba).\n"
              "Wir/Sie - czasownik zamienia się z zaimkiem wir/Sie.\n"
              "Ihr - odrzuca zaimek osobowy.")

imperative_endings = ("\nJak kończą się na -t, -d, -chn, -ffn, -tm, mają w 2os.l.p. końcówkę -e.\n"
                      "Czasowniki z samogłoską tematyczną e, w 2 i 3os.l.p. zamienia się na i lub ie "
                      "także nie otrzymują końcówki -e\n"
                      "Czasowniki z samogłoską tematyczną a, w 2 i 3os.l.p. zamienia się na ä i mogą "
                      "otrzymać końcówkę e.")

sports = {"das Aikido": "aikido", "der Basketball": "koszykówka", "das Boxen": "boks", "der Fussball": "piłka nożna",
          "das Gehen": "chód sportowy", "der Handball": "piłka ręczna", "der Hochsprung": "skok wzwyż",
          "das Hockey": "hokej", "das Judo": "judo", "Judo machen": "uprawiać judo", "das Karate": "karate",
          "der 100-m-Lauf": "bieg na 100 metrów", "das Laufen": "biegi", "der Marathon": "maraton",
          "das Schwimmen": "pływanie", "Ski alpin": "narciarstwo alpejskie", "das Skispringen": "skoki narciarskie",
          "die Sportart": "dyscyplina sportowa", "die Sportarten": "dyscypliny sportowe", "das Tennis": "tenis",
          "der Volleyball": "siatkówka", "der Weitsprung": "skok w dal"}

sports_usages = {"der Badeanzug": "strój kąpielowy", "die Badehose": "szorty kąpielowe", "der Ball": "piłka",
                 "die Bälle": "piłki", "der Boxhandschuh": "rękawica bokserska",
                 "die Boxhandschuhe": "rękawice bokserskie", "brauchen": "potrzebować",
                 "brauchen für": "potrzebować do",
                 "Ich brauche fürs Hockey einen Puck": "Do gry w hokeja potrzebuję krążka",
                 "der Hockeyschläger": "kij do hokeja", "der Puck": "krążek",
                 "der Schlittschuh": "łyżwa", "die Schlittschuhe": "łyżwy", "die Schwimmbrille": "okulary pływackie",
                 "die Sportkleidung": "strój sportowy", "der Sportschuh": "but sportowy",
                 "die Sportschuhe": "buty sportowe", "der Tennisschläger": "rakieta do tenisa",
                 "die Sonnenbrille": "okulary przeciwsłoneczne"}

monologues = ["Dobrze!", "Dobra odpowiedź!", "Świetnie!", "Co za geniusz!"]


class GermanWordsChecker:

    @classmethod
    def reversing_dict(cls, glossary):
        res_dict = dict()
        keys_list = list(glossary.keys())
        values_list = list(glossary.values())

        for indx in range(len(glossary)):
            res_dict[values_list[indx]] = keys_list[indx]
        return res_dict

    @classmethod
    def word_getter(cls, glossary, is_shuffle):
        good_answers = 0
        word_num = 0

        keys = list(glossary.keys())
        length = len(glossary)
        if is_shuffle:
            shuffle(keys)

        for word in keys:
            word_num += 1
            bad_answers = 0
            while True:
                answer = input(f"\n{word_num}/{length}. {word} - ")
                if answer == glossary[word]:
                    print(Fore.GREEN + choice(monologues) + Style.RESET_ALL)
                    if bad_answers == 0:
                        good_answers += 1
                    break
                else:
                    if bad_answers < 2:
                        print(Fore.RED + "O nie! Spróbuj jeszcze raz!" + Style.RESET_ALL)
                        bad_answers += 1
                    else:
                        print(Fore.RED + f"Oh...Chyba ci się nie udało( Przecież to jest {glossary[word].upper()}" +
                              Style.RESET_ALL)
                        break
        print(f"\nDobra sprawa! Dostałeś {Fore.RED + f"{good_answers}/{length}" + Style.RESET_ALL} punktów!")

    @classmethod
    def choice_chapter_words(cls):
        while True:
            print("\nWybierz rozdział:\n"
                  "0. Wróć\n"
                  f"1. Artykuły spożywcze ({len(groceries)} słów)\n"
                  f"2. Warzywa i owoce ({len(plants)} słów)\n"
                  f"3. Napoje ({len(drinks)} słów)\n"
                  f"4. Nazwy dań ({len(food)} słów)\n"
                  f"5. Określanie potrawy ({len(taste_and_appearance_of_food)} słów)\n"
                  f"6. Potrawy regionalne ({len(regional_dishes)} słów)\n"
                  f"7. Lokale gastronomiczne ({len(gastronomic_locals)} słów)\n"
                  f"8. Wyrażenia w sklepie/restauracji ({len(expressions)} słów)")
            answer2 = input("-----> ")
            match answer2:
                case "0":
                    break
                case "1":
                    cls.word_getter(cls.reversing_dict(groceries), True)
                case "2":
                    cls.word_getter(cls.reversing_dict(plants), True)
                case "3":
                    cls.word_getter(cls.reversing_dict(drinks), True)
                case "4":
                    cls.word_getter(cls.reversing_dict(food), True)
                case "5":
                    cls.word_getter(cls.reversing_dict(taste_and_appearance_of_food), True)
                case "6":
                    cls.word_getter(cls.reversing_dict(regional_dishes), True)
                case "7":
                    cls.word_getter(cls.reversing_dict(gastronomic_locals), True)
                case "8":
                    cls.word_getter(cls.reversing_dict(expressions), True)
                case _:
                    print("Wpisz liczbę od 0 do 7")

    @classmethod
    def variety_mochte(cls):
        mochte_forms = {"ich": "möchte", "du": "möchtest", "er/sie/es": "möchte", "wir": "möchten", "ihr": "möchtet",
                        "sie/Sie": "möchten"}
        cls.word_getter(mochte_forms, True)

    @classmethod
    def variety_nehmen(cls):
        nehmen_forms = {"ich": "nehme", "du": "nimmst", "er/sie/es": "nimmt", "wir": "nehmen", "ihr": "nehmt",
                        "sie/Sie": "nehmen"}
        cls.word_getter(nehmen_forms, True)

    @classmethod
    def variety_sich(cls):
        sich_forms = {"ich": "mich", "du": "dich", "er/sie/es": "sich", "wir": "uns", "ihr": "euch", "sie/Sie": "sich"}
        cls.word_getter(sich_forms, True)

    @classmethod
    def imperative_func(cls):
        imperative_forms = {"du": "odrzuca zaimek osobowy i końcówkę -st; ewentualnie dodaje końcówkę -e",
                            "wir/Sie": "czasownik zamienia się z zaimkiem wir/Sie",
                            "ihr": "odrzuca zaimek osobowy"}
        cls.word_getter(imperative_forms, True)

    @classmethod
    def imperative_endings_func(cls):
        imperative_endings_forms = {"jakie końcówki zamieniają się na -e": "-t, -d, -chn, -ffn, -tm",
                                    "sam. 'e' zamienia się na": "i/ie",
                                    "sam. 'a' zamienia się na": "ä"}
        cls.word_getter(imperative_endings_forms, True)

    @classmethod
    def grammar_theory(cls):
        while True:
            print("\n0. Wyjdź\n"
                  "1. Zaimek man\n"
                  "2. Froma möchte - chciałbym\n"
                  "3. Czasowniki zwrotne - sich - się\n"
                  "4. Tryb rozkazujący\n"
                  "5. Tryb rozkazujący - końcówki")
            answer = input("-----> ")
            match answer:
                case "0":
                    break
                case "1":
                    print(man)
                case "2":
                    print(mochte_form)
                case "3":
                    print(verbs)
                case "4":
                    print(imperative)
                case "5":
                    print(imperative_endings)
                case _:
                    print("Wpisz liczbę od 0 do 5")

    @classmethod
    def grammar_practice(cls):
        while True:
            print("\n0. Wyjdź\n"
                  "1. Odmiana möchte - chciałbym\n"
                  "2. Odmiana nahmen - brać\n"
                  "3. Odmiana sich - się\n"
                  "4. Tworzenie form trybu rozkazującego\n"
                  "5. Zamiana końcówek w trybie rozkazującym\n"
                  "6. Odmiana przykładów trybu rozkazującego")
            answer = input("-----> ")
            match answer:
                case "0":
                    break
                case "1":
                    cls.variety_mochte()
                case "2":
                    cls.variety_nehmen()
                case "3":
                    cls.variety_sich()
                case "4":
                    cls.imperative_func()
                case "5":
                    cls.imperative_endings_func()
                case "6":
                    ...
                case _:
                    print("Wpisz liczbę od 0 do 6")

    @classmethod
    def choice_chapter_grammar(cls):
        while True:
            print("\n0. Wyjdź\n"
                  "1. Teoria\n"
                  "2. Praktyka")
            answer = input("-----> ")
            match answer:
                case "0":
                    break
                case "1":
                    cls.grammar_theory()
                case "2":
                    cls.grammar_practice()
                case _:
                    print("Wpisz liczbę od 0 do 2")

    @classmethod
    def choice_type(cls):

        while True:
            print("\nCo chcesz powtórzyć?\n"
                  "0. Wyjdź\n"
                  "1. Słownictwo\n"
                  "2. Gramatyka")
            answer1 = input("-----> ")
            match answer1:
                case "0":
                    break
                case "1":
                    cls.choice_chapter_words()
                case "2":
                    cls.choice_chapter_grammar()
                case _:
                    print("Wpisz liczbę od 0 do 2")

    @classmethod
    def choice_type_sport(cls):
        while True:
            print("\n0. Wyjdź\n"
                  "1. Dyscypliny sportowe\n"
                  "2. Sprzęt sportowy\n"
                  "3. Czasowniki modalne")
            answer = input("-----> ")
            match answer:
                case "0":
                    break
                case "1":
                    cls.word_getter(cls.reversing_dict(sports), True)
                case "2":
                    cls.word_getter(cls.reversing_dict(sports_usages), True)
                case "3":
                    ...
                case _:
                    print("Wpisz liczbę od 0 do 3")

    @classmethod
    def choice_theme(cls):
        while True:
            print("\nWybierz temat:\n"
                  "0. Wyjdź\n"
                  "1. Jedzenie\n"
                  "2. Sport")
            answer = input("-----> ")
            match answer:
                case "0":
                    print(Fore.BLUE + "\nMiłej nauki!")
                    sleep(1.5)
                    break
                case "1":
                    cls.choice_type()
                case "2":
                    cls.choice_type_sport()
                case _:
                    print("Wpisz liczbę od 0 do 2")


words_checker = GermanWordsChecker()
words_checker.choice_theme()
