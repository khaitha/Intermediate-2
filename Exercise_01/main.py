from BankAccount import BankAccount

account = BankAccount("Rich Boy", 100000)

account.deposit(8000)

account.withdraw(1)

print(account.getBalance())