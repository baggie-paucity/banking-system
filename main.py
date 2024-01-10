from bank import Bank
from customer import Customer
from account import Account
from transaction import Transaction, TransactionType

def main():
    bank = Bank()

    customer1 = Customer("John Doe")
    customer2 = Customer("Jane Smith")

    account1 = Account(1000)
    account2 = Account(500)

    customer1.add_account(account1)
    customer2.add_account(account2)

    bank.add_customer(customer1)
    bank.add_customer(customer2)

    transaction1 = Transaction(customer1, account1, TransactionType.WITHDRAWAL, 200)
    transaction2 = Transaction(customer2, account2, TransactionType.DEPOSIT, 300)

    bank.process_transaction(transaction1)
    bank.process_transaction(transaction2)

    print("Customer 1 Balance:", account1.get_balance())
    print("Customer 2 Balance:", account2.get_balance())

if __name__ == "__main__":
    main()
