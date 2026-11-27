import numpy as np

'''example1'''
a = np.array([1,2,3])
b = np.array([3,4,5])
print(a)
print(b)
print()

print(a@b)
print()

'''example2'''
c = np.array([[1,2,],[3,4]])
d = np.array([[5,1],[2,4]])
print(c)
print(d)
print()

print(c@d)
print()

'''example3'''
e = [[1,2],[3,4]]
f = [[0,2,3],[1,1,5]]
print(e)
print(f)
print()

print(np.dot(e,f))
print()

'''example4'''
g = [[0,1,2],[2,1,1],[3,4,8]]
h = [5,1,2]
print(g)
print(h)
print()

print(np.dot(g,h))
print()

'''example5'''
i = [[1,0,1],[2,1,1],[2,2,3]]
j = [[1,1,2],[0,0,1],[4,1,5]]
print(i)
print(j)
print()

print(np.dot(i,j))