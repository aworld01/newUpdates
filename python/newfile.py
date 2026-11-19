def kwarg(**kwarg):
	print(kwarg, type(kwarg))
	
s = {'Abdul': 55, 'Mohan': 65,'Raju': 36,'Hena': 49}

kwarg(**s)