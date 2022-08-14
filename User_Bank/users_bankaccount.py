class BankAccount:
    def __init__(self, int_rate, balance, account_type):
        self.int_rate = int_rate
        self.balance = balance
        self.account_type = account_type

    @classmethod
    def instances(cls, int_rate, balance, account_type):
        return cls(int_rate, balance, account_type) 

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_info(self):
        print(f"\n Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + round(self.balance * self.int_rate, 2)
        return self
class User:

    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = {}

    def create_account(self, account_type, amount, interest):
        self.account[account_type] = BankAccount(amount, interest, account_type)
        return self
# Have to specify which account to change
    def make_deposit(self,amount):
        for key, value in self.account.items():
            print(key, ':', value)
        a = input("Which account do you want to deposit into?")
        while a not in self.account:
            print("This is not a valid account")
            a = input("Which account do you want to deposit into?")
            print(self.account)
        else:
            self.account[a] = self.account.deposit(amount)
# Have to specify which account to change
    def make_withdraw(self, amount):
        pass
# Have to specify which or all accounts
    def display_user_balance(self):
        pass

# Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# Add a transfer_money(self,amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account

peter = User('Peter', 'empty@gmail.com')
peter.create_account('checkings', 400, .02)
peter.make_deposit(100)