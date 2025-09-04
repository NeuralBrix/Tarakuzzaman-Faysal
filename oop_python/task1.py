class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. Your new balance is : {self.balance}")
        else: 
            print("Deposit amount must be an positive integer.")   

    def withdraw(self, amount):
        if isinstance(amount, int) and amount > 0:
            if amount <= self.balance:
                print(f"Withdrawn: {amount}. Your new balance is: {self.balance}")
            else: 
                print("You do not have enough balance")
        
        else:
            print("Withdraw amount must be a positive integer.")

account1 = BankAccount("Faysal", 100)
account1.withdraw(50)
account1.deposit(200)
account1.withdraw(500)

            

