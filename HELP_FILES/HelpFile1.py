# pendulum | arrow | datetime

from datetime import date, timedelta

current_date = date(2025, 12, 22)

while True:
    input("Kliknij Enter, aby przejść do następnego dnia...")
    current_date += timedelta(days=1)
    print(current_date)
