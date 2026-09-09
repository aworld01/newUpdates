"""
Create an Employee class with encapsulation:
	Attributes:
		name
		salary → private (__salary)
		
	Methods:
		get_salary() → returns salary
		increase_salary(amount) → adds amount.
		decrease_salary(amount) → subtracts amount but never below 0.
		
"""

class Employee:
	def __init__(self,name,salary):
		self.name = name
		self.__salary = salary
		
	def get_salary(self):
		print(f"Salary: {self.__salary}")
		
	def increase_salary(self,amount):
		if amount > 0:
			self.__salary += amount
			
	def decrease_salary(self,amount):
		if amount <= self.__salary:
			self.__salary -= amount
		else:
			print("Insufficient balance")
			
abdul = Employee("Abdul Zoha",1200)
abdul.get_salary()
print()

abdul.increase_salary(45000)
abdul.get_salary()
print()

abdul.decrease_salary(200)
abdul.get_salary()