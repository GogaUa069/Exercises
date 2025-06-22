number = int(input("-----> "))

one_ten = {1: 'one', 2: 'two', 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
eleven_nineteen = {11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
twenty_ninety = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}


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
