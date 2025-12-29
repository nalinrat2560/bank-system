class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("จำนวนเงินต้องมากกว่า 0")
            return
        self.balance += amount
        print(f"ฝากเงิน{amount}บาท สำเร็จ")

    def withdraw(self, amount):
        if amount <= 0:
            print("จำนวนเงินต้องมากกว่า 0")
            return
        if amount > self.balance:
            print("ยอดเงินไม่พอ")
            return
        self.balance -= amount
        print(f"ถอนเงิน{amount}บาท สำเร็จ")

    def show_balance(self):
        print(f"ยอดเงินคงเหลือ:{self.balance}บาท")

class SavingAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"เพิ่มดอกเบี้ย{interest:.2f}บาท")
