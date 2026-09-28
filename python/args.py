# *arg always returns a tuple

def arg(*arg):
	print(arg, type(arg))
	
if __name__ == "__main__":
	s = ['Abdul','mohan','Rajesh']
	t = ('Abdul','mohan','Rajesh')
	print(s, type(s))
	print(t, type(t))
	print()
	
	arg(s)
	arg(*s)
	arg(*t)