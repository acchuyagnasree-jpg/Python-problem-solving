class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: {interest}. New balance: {self.balance}"


# Example usage
try:
    acc1 = BankAccount("Alice", 500)
    print(acc1.deposit(200))
    print(acc1.withdraw(100))

    acc2 = SavingsAccount("Bob", 1000, 0.05)
    print(acc2.apply_interest())
    print(acc2.withdraw(300))
except ValueError as e:
    print("Error:", e)
