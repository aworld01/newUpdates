def fileOpener(arg):
	with open(arg, mode="r", encoding="utf-8") as rf:
		return rf.read()
		
#data = fileOpener('test.txt')

data = 'hello world! you? apple banana'
	
def aa(arg):
	wdTok = arg.split()
	return sorted(set(wdTok))

def ab(arg):
	bow = {'nil': 0}
	[bow.update({w:i}) for i, w in enumerate(aa(data), 1)]
	return bow
	
def ac(arg):
	rd = []
	n = ab(arg)
	d = arg.split()
	for i in d:
		if i in n:
			rd.append(n[i])
		else:
			rd.append('nil')
	return rd

g = ac("hello world! how are you? apple banana i am Abdul")

#dt = ab(wdTok)
#print(dt)
print(g)
