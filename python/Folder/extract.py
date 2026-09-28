file = "daily_use_sentences.txt"

def extract(path):
	with open(path,'r',encoding='utf-8') as f:
		#print(f.read()) #to print data
		
		'''convert all data into list item'''
		'''It splits data by newline'''
		#print(list(f))
		
		'''remove newline'''
		lines = [line.strip() for line in f]
		#print(lines)
		
		'''Remove empty list items'''
		nel = [line for line in lines if line]
		#print(nel)
		pairs = {}
		for i in range(0,len(nel)-1,2):
			english = nel[i]
			hindi = nel[i+1]
			#pairs.update({english:hindi})
			pairs[english] = hindi
		print((pairs))
		
extract(file)



















"""remove blank list item"""
#input = "a"
#if input:
#	print(input)

#fruits = ['Apple','orange','','banana','','mango']
#print(fruits)

#fruits = [fruit for fruit in fruits if fruit]
#print(fruits)