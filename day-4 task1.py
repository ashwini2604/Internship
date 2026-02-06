class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder} | Current Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        # Inherit attributes from parent
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of ${interest} added at {self.interest_rate}%. New balance: ${self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        # Inherit attributes from parent
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount} (Overdraft used). New balance: ${self.balance}")
        else:
            print("Transaction declined: Overdraft limit exceeded.")

# --- Testing the System ---

print("--- Testing Savings Account ---")
savings = SavingsAccount("Alice Moore", 1000, 5) # 5% interest
savings.display_balance()
savings.deposit(500)
savings.add_interest()
savings.withdraw(200)

print("\n--- Testing Current Account ---")
current = CurrentAccount("Bob Smith", 500, 1000) # $1000 overdraft limit
current.display_balance()
current.deposit(200)
# Testing overdraft: withdrawing more than the $700 balance
current.withdraw_with_overdraft(1200) 
current.display_balance()