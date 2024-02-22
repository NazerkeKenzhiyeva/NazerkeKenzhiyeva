class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        print(self.balance)
own=input()
balance = int(input())
x = int(input())
y = int(input())
account =Account(own, balance)
account.deposit(x)
account.withdraw(y)
