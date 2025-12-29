class Account:
    def __init__(self, ower, balance=0):
        self.ower = ower
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
