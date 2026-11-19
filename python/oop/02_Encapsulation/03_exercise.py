"""
Create a Wallet class:
	Attributes:
		owner
		__money (private)
		
	Methods:
		add(amount)
		spend(amount)
		check() → returns current money
		
Rules:
	Spending cannot make money negative
	Adding must be positive
"""
class Wallet:
	def __init__(self, owner, money):
		self.owner = owner
		self.__money = money
		
	def check(self):
		print(f"Your current balance: {self.__money}")
		
	def add(self, amount):
		if amount > 0:
			self.__money += amount
			
	def spend(self, amount):
		if amount <= self.__money:
			self.__money -= amount
			
abdul = Wallet("Abdul Zoha",5000)
abdul.check()

abdul.add(500)
abdul.check()

abdul.spend(1500)
abdul.check()