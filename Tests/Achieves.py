achieve_dict = {"New friend!": "Beat the game with the good ending.", "Unlucky": "Beat the game with the bad ending"}
dict_keys = list(achieve_dict.keys())
achieve_list = list()
endings = list()


def achieve_quest():
    print()
    print("Hahaha! Choose your side!")
    side = ""
    end = ""
    while side != "white" and side != "black":
        print("White - good; Black - bad!")
        side = input()
    if side == "white":
        end = "good"
    elif side == "black":
        end = "bad"
    if len(achieve_list) < 2:
        if end == "good" and end not in endings:
            achieve_list.append(f"{dict_keys[0]} - {achieve_dict[dict_keys[0]]}")
            if len(achieve_list) == 1:
                print("Achievement 1/2 received!")
                print(achieve_list[0])
                endings.append(end)
            elif len(achieve_list) == 2:
                print("Achievement 2/2 received!")
                print(achieve_list[1])
                endings.append(end)
        elif end == "good" and end in endings:
            print("Okay you chosen GOOD side, but you wont get the ACHIEVE")

        elif end == "bad" and end not in endings:
            achieve_list.append(f"{dict_keys[1]} - {achieve_dict[dict_keys[1]]}")
            if len(achieve_list) == 1:
                print("Achievement 1/2 received!")
                print(achieve_list[0])
                endings.append(end)
            elif len(achieve_list) == 2:
                print("Achievement 2/2 received!")
                print(achieve_list[1])
                endings.append(end)
        elif end == "bad" and end in endings:
            print("Okay you chosen BAD side, but you wont get the ACHIEVE")

    elif len(achieve_list) == 2 and end == "good":
        print("Okay you chosen GOOD side, but you wont get the ACHIEVE")
    elif len(achieve_list) == 2 and end == "bad":
        print("Okay you chosen BAD side, but you wont get the ACHIEVE")


def restart():
    question = ""
    while question != "q":
        while question != "q" and question != "p":
            print("Press 'q' to leave or 'p' to play")
            question = input()
        if question == "q":
            print("Bye!")
            break
        elif question == "p":
            achieve_quest()


achieve_quest()
restart()
