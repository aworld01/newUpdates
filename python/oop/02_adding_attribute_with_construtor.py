class Car:
	def __init__(self,brand,color):
		self.brand = brand #attribute
		self.color = color
		
my_car = Car("Toyota","White")
print(my_car.brand)
print(my_car.color)

"""
__init__: is a special function named constructor, it runs automatically when you create an object
"""