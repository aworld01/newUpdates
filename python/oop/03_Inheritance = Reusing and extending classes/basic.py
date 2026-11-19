'''
A parent class gives features to a child class.

Child class can add new features or override old ones.
'''
class Animal:
	def speak(self):
		print("Animal makes a sound...")
		
class Dog(Animal):
	'''override the speak() method'''
	def speak(self):
		print("Dog barks")
		
animal = Animal()
animal.speak()
dog = Dog()
dog.speak()
		
		