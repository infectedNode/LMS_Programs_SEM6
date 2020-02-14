class bank: 
	def __init__(self): 
		self.balance=0
		print("Account 'A' Created")

	def deposit(self):  
		amount=int(input("Enter an amount to Deposit\n")) 
		self.balance += amount 
		print("Balance= ",amount) 

	def withdraw(self): 
		amount = int(input("Enter an amount to Withdraw\n"))
		a=int(amount-self.balance)
		
		if self.balance>=amount: 
			self.balance-=amount 
			print("Balance = ", self.balance) 
		else:
			print("Insufficient fund of",a)
			print("balance", self.balance)

obj1 =bank() 
obj1.deposit() 
obj1.withdraw() 
