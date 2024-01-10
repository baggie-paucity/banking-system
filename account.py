class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
