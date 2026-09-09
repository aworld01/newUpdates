file = "daily_use_sentences.txt"

def ext(path):
	with open(path,'r',encoding='utf-8') as f:
		data = f.read()
		#print(data)
		lines = [line.strip() for line in f]
		print(lines)
		
		
ext(file)