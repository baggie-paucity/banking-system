class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def process_transaction(self, transaction):
        transaction.process()
