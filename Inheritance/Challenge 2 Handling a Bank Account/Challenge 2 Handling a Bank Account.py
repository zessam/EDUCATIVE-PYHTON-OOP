class Account:   # parent class
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    # this method just returns the value of balance
    def getBalance(self):
        return self.balance

    # deposit method adds the amount to the balance
    def deposit(self, amount=None):
        self.balance = self.balance + amount

    # withdrawal method subtracts the amount from the balance
    def withdrawal(self, amount=None):
        self.balance = self.balance - amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        self.interestRate = interestRate
        super().__init__(title, balance)

    # computes interest amount using the interest rate
    def interestAmount(self):
        interestAmount = ((self.interestRate*self.balance)/100)
        return (self.balance * self.interestRate / 100)


obj1 = SavingsAccount("Zeyad", 5000, 10)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(1000)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())
