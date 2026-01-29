from BETA_Games.GlobalWarFrontline.FILES.MainFiles.SysConfig import system
from BETA_Games.GlobalWarFrontline.FILES.MainFiles.MAIN import pass_func


class LoanConfig:
    error_comm1 = system.communicate("ERROR: Enter INTEGER in range 1-500.000", "LIGHTRED_EX")
    loans_limit = 5
    cash_limit = 500_000

    def __init__(self):
        self.loans = 0
        self.loan_sum = 0
        self.loans_left = self.loans_limit - self.loans
        self.error_comm2 = system.communicate(f"ERROR: Enter INTEGER in range 1-{self.loan_sum}")

    def __validate_loans(self):
        return self.loans_left > 0

    def take_out_loan(self):
        if self.__validate_loans():
            while True:
                amount = 0
                try:
                    amount = int(input(system.communicate("Enter amount (1-500.000): $", "LIGHTWHITE_EX")))
                except amount not in range(1, 500_001):
                    print(self.error_comm1)
                except TypeError:
                    print(self.error_comm1)
                else:
                    break
            self.loans += 1
            self.loan_sum += amount
        else:
            print(system.communicate("ERROR: Reached maximum amount of loans!", "LIGHTRED_EX"))

    def repay_loan(self):
        if not self.__validate_loans():
            while True:
                amount = 0
                try:
                    amount = int(input(system.communicate(f"Enter amount (1-{self.loan_sum})")))
                except amount not in range(1, self.loan_sum+1):
                    print(self.error_comm2)
                except TypeError:
                    print(self.error_comm2)
                else:
                    break
            self.loans -= 1
            self.loan_sum -= amount
        else:
            print(system.communicate("ERROR: You have all your debts paid off."))


loan = LoanConfig()
take_money = system.Option(f"Take out a loan (loans left: {loan.loans_left}/5)", loan.take_out_loan)
give_money = system.Option(f"Repay a loan (sum left: ${loan.loan_sum})", loan.repay_loan)
from_loan_to_economy = system.Option("Back - ECONOMY", pass_func)

loan_menu = system.Menu("LOAN OPERATIONS", (take_money, give_money))
loan_menu()
