class BankAccount:
    def __init__(self,balance=0.0):
        self.balance=balance
    
    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount must be positive.")
            return
        self.balance+=amount
        print(f"Deposited {amount:.2f}, current balance {self.balance:.2f}")
    
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid amount.")
            return
        if amount>self.balance:
            print("Insufficient funds.")
            return
        self.balance-=amount
        print(f"Withdraw {amount:.2f},current balance {self.balance:.2f}")

class SavingAccount(BankAccount):
    def __init__(self,balance=0.0,min_balance=0.0):
        super().__init__(balance)
        self.min_balance=min_balance
    
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid withdrawal amount.")
            return
        if self.balance-amount<self.min_balance:
            print(f"Withdrawal denied, balance cannot go below {self.min_balance:.2f}")
            return
        self.balance-=amount
        print(f"Withdrew amount: {amount:.2f}, current balance: {self.balance:.2f}")

def get_positive(target):
    while True:
        try:
            value=float(input(target))
            if value<=0:
                print("Invalid amount.")
            else:
                return value
        except ValueError:
            print("Invalid character, please enter a number")

set_users_balance=get_positive("Please enter the initial balance: ")
min_balance=get_positive("Please enter the minimum balance: ")
account=SavingAccount(set_users_balance,min_balance)
while True:
    print("\n---Menu---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice=input("Choose an option: ")
    if choice=="1":
        amount=get_positive("Deposit amount: ")
        account.deposit(amount)
    elif choice=="2":
        amount=get_positive("Withdrawal amount: ")
        account.withdraw(amount)
    elif choice=="3":
        print(f"Current balance: {account.balance:.2f}")
    elif choice=="4":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")