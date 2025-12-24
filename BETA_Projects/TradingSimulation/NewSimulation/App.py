from random import choices
from secrets import randbelow
from datetime import date, timedelta
from forex_python.converter import CurrencyRates
import asciichartpy

c = CurrencyRates()


class Currency:
    def __init__(self, code: str, amount: float):
        self.code = code
        self.amount = amount

    def get_rate(self, other, rate_date):
        return c.get_rate(self.code, other.code, rate_date)


class Pocket:
    def __init__(self):
        self.USD = Currency("USD", 1000.00)
        self.EUR = Currency("EUR", 0.00)
        self.PLN = Currency("PLN", 0.00)

    @staticmethod
    def transfer_currency(current: Currency, other: Currency, amount: float):
        other.amount = round(other.amount + c.convert(current.code, other.code, amount), 2)
        current.amount = round(current.amount - amount, 2)


class Settings:
    ...


class Account:
    ...


class App:
    ...
