'''
Create a parent class Person:
	Attributes:
		name
		age
		
	method:
		info() => print name and age.
		
Create a child class Employee that inherits from Person:
		Additional attribute:
			salary
			
		Additional method:
			details() → prints name, age, salary
'''
class Person:
		def __init__(self, name, age):
			self.name = name
			self.age = age
			
		def info(self):
			print(f'{self.name} {self.age}')
			
class Employee(Person):
		def __init__(self, name, age, salary):
			super().__init__(name, age)
			self.salary = salary
			
		def details(self):
			print(f"{self.name} {self.age} {self.salary}")
			
p = Person("Abdul Zoha",34)
p.info()

e = Employee("Abdul Zoha",34,25000)
e.details()