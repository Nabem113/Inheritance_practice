from account import Account


class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)


# trial operation
currentAccount = CurrentAccount()
print(currentAccount.deposit(1000))
