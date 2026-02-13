class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self,balance=0.0):
        if balance<0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount<=0:
            raise InvalidAmountError("Withdraw amount must be positive.")
        if amount>self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance-=amount
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self,balance=0.0,min_balance=0.0):
        if min_balance<0:
            raise InvalidAmountError("Minimum balance cannot be negative.")
        super().__init__(balance)
        self.min_balance=min_balance
    def withdraw(self, amount):
        if amount<=0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if self.balance-amount<self.min_balance:
            raise InsufficientFundsError(f"Balance cannot go below {self.min_balance:.2f}")
        self.balance-=amount
        return self.balance

def get_positive(target):
    while True:
        try:
            value=float(input(target))
            if value<=0:
                print("Amount must be positive.")
            else:
                return value
        except ValueError:
            print("Invalid input.")

def main():
    try:
        initial_balance=get_positive("Enter initial balance: ")
        min_balance=get_positive("Enter the minimum balance: ")
        account=SavingAccount(initial_balance,min_balance)
    except InvalidAmountError as e:
        print(f"Error creating account: {e}")
        return
    while True:
        print("\n---Menu---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check current balance")
        print("4. Exit")
        choice=input("Choose an option: ")
        if choice=="1":
            amount=get_positive("Deposit amount: ")
            try:
                new_balance=account.deposit(amount)
                print(f"Deposit successful, current balance: {new_balance:.2f}")
            except InvalidAmountError as e:
                print(f"Error: {e}")
        elif choice=="2":
            amount=get_positive("Withdrawal amount: ")
            try:
                new_balance=account.withdraw(amount)
                print(f"Withdrawal successful, current balance {new_balance:.2f}")
            except (InvalidAmountError,InsufficientFundsError) as e:
                print(f"Error: {e}")
        elif choice=="3":
            print(f"Current balance: {account.balance:.2}")
        elif choice=="4":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__=="__main__":
    main()
