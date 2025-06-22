number = int(input("-----> "))

one_ten = {1: 'один', 2: 'два', 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять"}
eleven_nineteen = {11:"одинадцать",12:"двенадцать",13:"тринадцать",14:"четырнадцать",15:"пятнадцать",16:"шестнадцать",17:"семнадцать",18:"восемнадцать",19:"девятнадцать"}
twenty_ninety = {2:"двадцать",3:"тридцать",4:"сорок",5:"пятьдесят",6:"шестьдесят",7:"семдесят",8:"восемьдесят",9:"девяносто"}


def num_to_str(num):
    if 1 <= num <= 10:
        print(one_ten[num])
    elif 11 <= num <= 19:
        print(eleven_nineteen[num])
    elif 20 <= num <= 99:
        first_num = num // 10
        second_num = num % 10
        if second_num == 0:
            print(twenty_ninety[first_num])
        else:
            print(f"{twenty_ninety[first_num]} {one_ten[second_num]}")


num_to_str(number)
