from enum import Enum

class TransactionType(Enum):
    DEPOSIT = 1
    WITHDRAWAL = 2

class Transaction:
    def __init__(self, customer, account, transaction_type, amount):
        self.customer = customer
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

    def process(self):
        if self.transaction_type == TransactionType.DEPOSIT:
            self.account.deposit(self.amount)
        elif self.transaction_type == TransactionType.WITHDRAWAL:
            self.account.withdraw(self.amount)
