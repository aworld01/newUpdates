'''
data = 'I like ball because I like cricket'

tokenization = ['I', 'like', 'ball', 'because', 'I', 'like',  'cricket']

max_sequence_length = 7

vocab = {'cricket', 'like', 'because', 'I', 'ball'}

vocabularyMapping = {'cricket': 0, 'like': 1, 'because': 2, 'I': 3, 'ball': 4}
'''
data = 'I like ball because I like cricket'

token = data.split()
#print(token)

max_sequence_length = len(token)
#print(max_sequence_length)

'''method 1'''
#vocab = []
#for i in token:
#	if i not in vocab:
#		vocab.append(i)

'''method 2'''		
#vocab  = []
#[vocab.append(i) for i in token if i not in vocab]
#print(vocab)

'''method 3'''
vocab = set(token)
#print(vocab)

'''method 1'''
#vocabMapping = {}
#for index, item in enumerate(vocab):
#	vocabMapping.update({item: index})
	
'''method 2'''
vocabMapping = {item: index for index, item in enumerate(vocab)}
	
print(vocabMapping)