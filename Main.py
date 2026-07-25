class DateError(Exception):
    pass


class DateString(DateError):
    def __init__(self, date_string: str):
        self.date_string = date_string

    def validate_date(self):
        split_date = self.date_string.split(".")
        if len(split_date) != 3 or int(split_date[0]) not in range(1, 32) or int(split_date[1] not in range(1, 13)), :
            raise DateError()

    def __str__(self):
        split_date = self.date_string.split(".")
        day = split_date[0].rjust(2, "0")
        month = split_date[1].rjust(2, "0")
        year = split_date[2]
        return f"{day}.{month}.{year}"


date_string = input()

try:
    date = DateString(date_string)
except DateError:
    print("Неверный формат даты")
else:
    print(date)
