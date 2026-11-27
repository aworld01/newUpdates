import numpy as np

x = np.array([2,1,4,3])

w = np.array([
[0.2,0.3,0.1,0.5],
[0.8,0.7,0.6,0.2],
[0.4,0.9,0.2,0.5]
])
b = np.array([1,3,7])

w2 = np.array([0.3,0.4,0.1])
b2 = np.array(0.4)

logit = w@x+b
print(f'logit => {logit}')
print()
    
def sigmoid(x):
    return 1/(1+np.exp(-x))

h1 = sigmoid(logit)

print(f'h1 => {h1}')
print()

logit2 = w2@h1+b2
print(f'logit2 => {logit2}')
y_pred = sigmoid(logit2)
print()
print(f'y_pred => {y_pred}')


#import math

#def sig(x):
#    return 1/(1+(math.e**-x))
#    
#y_pre= sig(logit)