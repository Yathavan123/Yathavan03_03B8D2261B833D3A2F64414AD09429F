class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")

    def display_details(self):
        return f"Account Number: {self.__account_number}\nAccount Holder Name: {self.__account_holder_name}\nAccount Balance: {self.__account_balance}"


# Get user input for account details
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

# Create an instance of BankAccount
account = BankAccount(account_number, account_holder_name, initial_balance)

# Deposit money
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

# Withdraw money
withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

# Display account details
details = account.display_details()
print(details)
