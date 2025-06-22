def get_nod(a, b):

    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a

    print(a)


get_nod(int(input()), int(input()))
