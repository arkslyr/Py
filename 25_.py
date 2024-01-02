class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive amount.")
        else:
            print("Insufficient funds for withdrawal.")

# Example usage:
account1 = BankAccount(123456, "John Doe", "Savings", 1000)

# Deposit
account1.deposit(500)

# Withdrawal
account1.withdraw(200)

# Try to withdraw more than the balance
account1.withdraw(9000)
