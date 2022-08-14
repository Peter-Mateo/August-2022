import math
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


account1 = BankAccount(.03, 100)

#Create a new account deposit 3 times withdraw 1 time and yield_interest
account1.deposit(10)
account1.deposit(10)
account1.deposit(10)
account1.withdraw(15)
account1.yield_interest()
account1.display_info()

#Create a second account make 2 deposits 4 withdraws, then yield_interest and display_info using chaining 
account2 = BankAccount(.03, 100)
account2.deposit(100).deposit(10).withdraw(10).withdraw(1).withdraw(55).withdraw(10).yield_interest().display_info()

#Instance Check
account3 = BankAccount.instances(.04, 100)
account3.all()
