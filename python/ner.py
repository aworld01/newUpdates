from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio() * 100

def maxMatch(usr,data):
	temp = {}
	
	for sent in data:
		temp.update({similarity(sent,usr):sent})
	m = max(temp.keys())
	return temp[m], m

if __name__=='__main__':
    names = {"Abdul Zoha": "अब्दुल ज़ोहा","Sarwar": "सरवर","Hameed": "हमीद", "Patna": "पटना"}
    
    keys = names.keys()

    inp = "My name is Abdul"
    inp = "I am going to patna"
    
    #name = maxMatch(inp,names)
#    print(name[0])
    
    name = maxMatch(inp,keys)
    print(f"मेरा नाम {names[name[0]]} है")