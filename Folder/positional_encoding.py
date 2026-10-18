import math

d_model = 4
pos = 1
i = 0

'''simple equation'''
a = i/d_model
#print(f'   {a}')

b = 10000**a
#print(f'   {b}')

c = pos/b
#print(f'   {c}')

sin = math.sin(c)
print(f'    sin => {sin}')

cos = math.cos(c)
print(f'    cos => {cos}')


'''complex equation'''
x = pos/(10000**(i/d_model)) #1
#print(f'   {x}')

sin = math.sin(x)
print(f'    sin => {sin}')

cos = math.cos(x)
print(f'    cos => {cos}')





d_model = 4
pos = 1
i = 1

x = pos/(10000**(i/d_model))
#print(f'   {x}')

y = math.sin(x)
#print(f'   {y}')


