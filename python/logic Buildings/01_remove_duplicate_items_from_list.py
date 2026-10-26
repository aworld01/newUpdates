data = "I like ball because I like cricket"

tok = data.split()
print(tok)

'''method_01 (works but slow'''
vocab = []
[vocab.append(i) for i in tok if i not in vocab]
print(vocab)

'''method_02 (code in oneline)'''
vocab = []; [vocab.append(i) for i in tok if i not in vocab]
print(vocab)

'''method_03 (fast and pythonic)'''
vocab = list(dict.fromkeys(tok))
print(vocab)

'''method_04 (fastest but not order maintained'''
vocab = list(set(tok))
print(vocab)

total = len(tok)
print(total)


'''Vocabulary Indexing'''
'''method_01'''
token2id = {item: idx for idx, item in enumerate(vocab)}
print(token2id)

'''method_02'''
token2id = dict(zip(vocab, range(len(vocab))))
print(token2id)
