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

    # print(f"Account '{self.name}' created. \nBalance = €{self.balance:.2f} ")

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

    def withdraw(self, amount):
        try:
            self.transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw completed. :weißes_häkchen:")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: :x: {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n*****\n\nBeginning Transfer... :rakete: ")
            self.transaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print(f"\nTransfer completed! :weißes_häkchen:\n\n*****")
        except BalanceException as error:
            print(f"\nTransfer interrupted: :x: {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\Withdraw interrupted: {error}")
