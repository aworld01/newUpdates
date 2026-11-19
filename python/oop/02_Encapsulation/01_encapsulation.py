'''
Protecting data and giving controlled access.

1. Private attributes => self.__balance
2. Getter methods => get_balance()
3. Setter methods => set_balance()
'''
'''Bank Account (Encapsulation)'''
class bankAccount:
	def __init__(self, owner, balance):
		self.owner = owner
		self.__balance = balance #private attribute
		
	def get_balance(self):
		print(self.__balance)
		
	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			
	def withdraw(self, amount):
		if amount <= self.__balance:
			self.__balance -= amount
		else:
			print("Insufficient balance")
			
abdul = bankAccount("Abdul Zoha",5000)
abdul.get_balance()
print()

abdul.deposit(500)

abdul.get_balance()
print()

abdul.withdraw(1000)
abdul.get_balance()