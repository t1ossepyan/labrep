class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum):
        self.balance += sum
        print(f"Deposited {sum}. New balance: {self.balance}")

    def withdraw(self, sum):
        if sum > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= sum
            print(f"Withdrew {sum}. New balance: {self.balance}")

