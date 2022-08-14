class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    @classmethod
    def instances(cls, int_rate, balance):
        return cls(int_rate, balance) 

    def all(self):
        print(self.int_rate, self.balance)

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
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + round(self.balance * self.int_rate, 2)
        return self
class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    #Other methods
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_info()
        return self

# Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# Add a transfer_money(self,amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account 