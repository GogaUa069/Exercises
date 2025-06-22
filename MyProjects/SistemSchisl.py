system = int(input("Select system: "))
number = int(input("Enter number: "))
converted_num = list()


def converting(num, sys):
    while num != 0:
        x = num % system
        if x >= 10:
            sym = chr(87 + x)
            converted_num.insert(0, str(sym.upper()))
        else:
            converted_num.insert(0, str(x))
        num = num // system

    print("".join(converted_num))


converting(number, system)
