from dataclasses import dataclass

class BalanceException(Exception):
    pass

@dataclass
class BankAccount:
    # def __init__(self, initialAmount, acctName):
    #     self.balance = initialAmount
    #     self.name = acctName

    balance: int
    name: str

        #print(f"Account '{self.name}' created. \nBalance = €{self.balance:.2f} ")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = €{self.balance:.2f}")

    def deposite(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit completed. ")
        self.getBalance()

    def transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry. Account '{self.name}' only has a balance of €{self.balance:.2f}"
            )
