from Insufficent_funs import InsufficientFundsError

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawn: ${amount}. New Balance: ${self.balance}")


try:
    acc = BankAccount(5000)
    acc.withdraw(6000)
except InsufficientFundsError as e:
    print(e)
finally:
    print("Transaction completed!")