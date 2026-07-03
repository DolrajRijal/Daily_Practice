class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited £{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew £{amount}")

    def display_balance(self):
        print(f"Current balance: £{self.balance}")


account = BankAccount("Ram", 1000)

account.deposit(500)
account.withdraw(200)
account.display_balance()