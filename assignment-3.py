'''
    Assignment 3 bank application
'''
# Part II: Business Logic
class Account:
    def __init__(self, account, balance):
        self.account_number = account
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount cannot be negative")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, account_number, balance, min_balance):
        Account.__init__(self, account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount cannot be negative")
        elif self.balance - amount < self.min_balance:
            print("Withdrawal exceeds minimum balance")
        else:
            Account.withdraw(self, amount)

class ChequingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        Account.__init__(self, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount cannot be negative")
        elif amount > (self.balance + self.overdraft_limit):
            print("Withdrawal exceeds available balance and overdraft limit")
        else:
            Account.withdraw(self, amount)

class Bank:
    def __init__(self):
        self.accounts = []
        self.account_counter = 1  # Separate counter for account numbers

    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise ValueError("Account not found")

    def open_account(self, account_type, initial_balance, *additional_params):
        try:
            if account_type.lower() == "savings":
                min_balance = float(additional_params[0])
                account = SavingsAccount(account_number=self.account_counter, balance=initial_balance, min_balance=min_balance)
            elif account_type.lower() == "chequing":
                overdraft_limit = float(additional_params[0])
                account = ChequingAccount(account_number=self.account_counter, balance=initial_balance, overdraft_limit=overdraft_limit)
            else:
                raise ValueError("Invalid account type")
        except ValueError as e:
            raise e

        self.accounts.append(account)
        print(f"Account opened successfully. Account Number: {account.account_number}")
        self.account_counter += 1  # Increment account number counter
        return account

# Part I: User Interaction
class Program:
    def __init__(self, bank):
        self.bank = bank
        self.current_account = None

    def show_main_menu(self):
        while True:
            print("Main Menu:")
            print("1. Open Account")
            print("2. Select Account")
            print("3. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 1:
                account_type = input("Enter account type (Savings or Chequing): ").lower()
                initial_balance_str = input("Enter initial balance: ")
                try:
                    initial_balance = float(initial_balance_str)
                except ValueError:
                    print("Invalid input for initial balance. Please enter a number.")
                    continue

                try:
                    if account_type == "savings":
                        min_balance_str = input("Enter minimum balance: ")
                        min_balance = float(min_balance_str)
                        self.bank.open_account(account_type, initial_balance, min_balance)
                    elif account_type == "chequing":
                        overdraft_limit_str = input("Enter overdraft limit: ")
                        overdraft_limit = float(overdraft_limit_str)
                        self.bank.open_account(account_type, initial_balance, overdraft_limit)
                    else:
                        print("Invalid account type")
                except ValueError as e:
                    print(e)
            elif choice == 2:
                self.display_accounts()
                account_number_str = input("Enter account number: ")
                try:
                    account_number = int(account_number_str)
                    self.current_account = self.bank.search_account(account_number)
                    self.show_account_menu()
                except ValueError as e:
                    print(e)
            elif choice == 3:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_accounts(self):
        print("Available Accounts:")
        for account in self.bank.accounts:
            print(f"Account Number: {account.account_number}, Type: {type(account).__name__}")

    def show_account_menu(self):
        while True:
            print("Account Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 1:
                print(f"Balance: {self.current_account.balance}")
            elif choice == 2:
                amount_str = input("Enter deposit amount: ")
                try:
                    amount = float(amount_str)
                    self.current_account.deposit(amount)
                    print("Deposit successful.")
                except ValueError as e:
                    print(e)
            elif choice == 3:
                amount_str = input("Enter withdrawal amount: ")
                try:
                    amount = float(amount_str)
                    self.current_account.withdraw(amount)
                    print("Withdrawal successful.")
                except ValueError as e:
                    print(e)
            elif choice == 4:
                print("Exiting Account Menu.")
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        print("Welcome to the Bank!")
        self.show_main_menu()

# Create Bank and Program instances
bank = Bank()
program = Program(bank)

# Run the program
program.run()
