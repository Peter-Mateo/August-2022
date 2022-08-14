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