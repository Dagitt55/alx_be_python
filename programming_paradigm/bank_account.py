# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.account_balance:
            print("Insufficient funds for withdrawal.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
