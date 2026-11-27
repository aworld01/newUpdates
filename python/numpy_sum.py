import numpy as np

x1 = 2

x2 = [4.8,1.21,2.385]

x3 = [[4.8,1.21,2.385],
          [8.9,1.81,0.2],
          [1.41,1.051,0.026]]
          
exp_value = np.exp(x1)
exp_values2 = np.exp(x2)
exp_values3 = np.exp(x3)

print(x1)
print(x2)
print(x3)
print()


print(exp_value)
print(exp_values2)
print(exp_values3)
print()

sum1 = np.sum(x2)
sum2 = np.sum(x3)
sum3 = np.sum(x3,axis=0)
sum4 = np.sum(x3,axis=1)
sum5 = np.sum(x3,axis=1,keepdims=True)

print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)