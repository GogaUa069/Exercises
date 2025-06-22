def create_variable(name, value):
    my_dict = dict()
    my_dict[name] = value
    print(f"Переменная {name} сохранена со значением: {value}")
    return my_dict


variables = create_variable("Password", "Egor_1412")
print(variables["Password"])
