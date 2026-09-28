'''
01. Create a class Product with attributes:
    name
    price
    quantity

02. Add method total_price that returns price * quantity.
    
03. Create an object:
	Product("Keyboard", 50, 2)
	
04. Print:
	Product name
	Total price (should be 100)
'''
class Product:
	def __init__(self,name,price,quantity):
		self.name = name
		self.price = price
		self.quantity = quantity
		
	def total_price(self):
		print(f'Product name: {self.name}')
		print(f'Total price: {self.price*self.quantity}')
		
keyboard = Product("Keyboard",50,2)
keyboard.total_price()