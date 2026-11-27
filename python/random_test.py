import numpy as np

print('Value between 0 to 1:-')
print(np.random.rand(2))
print()

print(np.random.rand(2,3))
print()
print()

print("Positive or negative numbers close to zero:-")
print(np.random.randn(2))
print()

print(np.random.randn(2,3))
print()
print()

print(np.random.ranf(2))
print()

print(np.random.ranf((2,3)))
print()
print()

'''0-10'''
np.random.randint(100)

"""np.randint(min,max,total_value)"""
print(np.random.randint(2,6,10))
print(np.random.randint(2,3,(3,2)))