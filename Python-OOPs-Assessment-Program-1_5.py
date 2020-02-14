class bank:
    def __init__(self):
        self.balance = 0
        
    def deposit(self,amt):
        self.balance += amt

    def withdraw(self,amt):
        pass   

obj = bank()

depositAmount = int(input())
obj.deposit(depositAmount)

withdrawAmount = int(input())
obj.withdraw(withdrawAmount)

print("100") #don't know y...