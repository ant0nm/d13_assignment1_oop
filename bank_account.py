class BankAccount:

    """ A class representing a simple bank account """

    # class variables
    interest_rate = 0.01
    accounts = []

    # class methods
    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total += account.balance
        return total

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate

    # instance methods
    def __init__(self, balance = 0):
        # instance variables
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

# test out the bank account class
my_account = BankAccount.create()
your_account = BankAccount.create()
print("My initial balance:")
print(my_account.balance)
print("Total funds in the bank:")
print(BankAccount.total_funds())

my_account.deposit(200)
your_account.deposit(1000)
print()
print("My account after 200 deposit:")
print(my_account.balance)
print("Your account after 1000 deposit:")
print(your_account.balance)
print("Total funds in the bank after 2 deposits:")
print(BankAccount.total_funds())

BankAccount.interest_time()
print()
print("My account after adding interest:")
print(my_account.balance)
print("Your account after adding interest:")
print(your_account.balance)
print("Total funds in the bank after adding interest:")
print(BankAccount.total_funds())

my_account.withdraw(50)
print()
print("My account after a withdrawal:")
print(my_account.balance)
print("Total funds in the bank after a withdrawal:")
print(BankAccount.total_funds())
