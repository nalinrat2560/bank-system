class Account:
    def __init__(self, ower, balance=0):
        self.ower = ower
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("จำนวนเงินต้องมากกว่า 0")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("ถอนเงินไม่ได้")
            return
        self.balance -= amount