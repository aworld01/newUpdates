'''
even => PE(pos,2i) = sin(pos/10000**2i/d)

odd => PE(pos,2i+1) = cos(pos/10000**2i/d)

even => PE(pos,i) = sin(pos/10000**i/d_model)

odd => PE(pos,i) => cos(pos/10000**(i-1)/d_model)

token = ['I', 'like', 'ball', 'because', 'I', 'like', 'cricket']

max_sequence_length = 7

vocab = ['I', like, 'ball', 'because', 'cricket']

'''
import math

#data = 'I like ball because I like cricket'
#token = data.split()
#max_sequence_length = len(token)
#vocab = set(token)
#dict = {}

#for index, item in enumerate(vocab):
#	dict.update({index: item})

#print(dict)

d_model = 6
i = [0,1,2,3,4,5,6]

even = 10000**(0.02/d_model)
print(even)

odd = 10000**((0.73-1)/d_model)
print(odd)