class BankAccount:

    # Class-level counter
    account_counter = 1000

    # Constructor
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

        print("\nAccount created for", self.account_holder)
        print("Account Number:", self.account_number)

    # Deposit
    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    # Withdraw
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Error: Insufficient balance.")

    # Display balance
    def display_balance(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

    # Transfer
    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount

            print(amount, "transferred successfully to",
                  other_account.account_holder)
        else:
            print("Error: Insufficient balance for transfer.")

    # Destructor
    def __del__(self):
        print("Account", self.account_number, "is deleted.")


# Taking input from user
name1 = input("Enter first account holder name: ")
name2 = input("Enter second account holder name: ")

# Creating two objects
account1 = BankAccount(name1)
account2 = BankAccount(name2)


# Deposit into first account
print("\n--- Deposit in Account 1 ---")
amount = float(input("Enter deposit amount: "))
account1.deposit(amount)


# Withdraw from first account
print("\n--- Withdraw from Account 1 ---")
amount = float(input("Enter withdrawal amount: "))
account1.withdraw(amount)


# Transfer from account 1 to account 2
print("\n--- Transfer Money ---")
amount = float(input("Enter transfer amount: "))
account1.transfer(amount, account2)


# Display both accounts
print("\n--- Account 1 Details ---")
account1.display_balance()

print("\n--- Account 2 Details ---")
account2.display_balance()


# Withdraw from second account
print("\n--- Withdraw from Account 2 ---")
amount = float(input("Enter withdrawal amount from Account 2: "))
account2.withdraw(amount)


# Final balances
print("\n--- Final Account Details ---")
account1.display_balance()
account2.display_balance()