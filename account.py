class Account:

    def __init__(self):
        self.accountBalance = 40000
        self.accountName = "Benedict"
        self.accountNumber = 2245798904

    def deposit(self, amount):
        self.accountBalance = self.accountBalance + amount
        return f"Your new ammount is {self.accountBalance}"

    def withdraw(self, amount):
        self.accountBalance = self.accountBalance - amount
        return f"Your current account balance is now {self.accountBalance}"
