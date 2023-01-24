class BankAccount:    
    def __init__(self,accountName, startingBalance):
        self.accountName = accountName
        self.balance = startingBalance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def getBalance(self):
        return "{} has a balance of {}".format(self.accountName, self.balance)