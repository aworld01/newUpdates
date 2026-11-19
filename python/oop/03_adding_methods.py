'''
methods are functions inside a class
'''
class Car:
	def __init__(self,brand,color):
		self.brand = brand
		self.color = color
		
	'''adding method'''
	def describe(self):
		print(f'This car is {self.color} {self.brand}')
		
my_car = Car("Toyota","White")
my_car.describe()