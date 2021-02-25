class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# * Inheritance
class CheckingAccount(Account):
    # __doc__ text : info about the Class
    """ This class generates checking account """

    # * Class variable (static)
    type = 'checking'

    def __init__(self, filepath, transaction_fee):
        Account.__init__(self, filepath)
        self.transaction_fee = transaction_fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.transaction_fee

# account = Account('balance.txt')
# print(account.balance)

# account.withdraw(100)
# print(account.balance)

# account.deposit(200)
# print(account.balance)

# account.commit()

account = CheckingAccount('balance.txt', 1)
account.transfer(100)
print(account.balance)
account.commit()

print(account.__doc__)