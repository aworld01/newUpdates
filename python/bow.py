import numpy as np
from tok import token, stem

#def bow(tok,voc):
#    bag = np.zeros(len(voc),dtype=np.float32)
#    for i,w in enumerate(tok):
#        if w in voc:
#            bag[i] = 1
#    return bag


def BoW(tok,voc):
    sent = [stem(word) for word in tok]
    bag = np.zeros(len(voc), dtype=np.float32)
    for i,w in enumerate(voc):
        if w in sent:
            bag[i] = 1
    return bag

if __name__=='__main__':
    v = ['this','is','an','apple','red','green']
    t = ['this','is','a','mango','is','red','and','hi']
    print(BoW(t,v))