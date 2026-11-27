import re

s = '''
Country code: +91
Mobile number: +919006228083
'''

#p = r'\d'
#result = re.findall(p, s)
#print(result)
#print()

#p = r'\d\d'
#result = re.findall(p, s)
#print(result)
#print()

#p = r'\d\d\d'
#result = re.findall(p, s)
#print(result)
#print()

#p = r'\d\d\d\d\d\d\d'
#result = re.findall(p, s)
#print(result)
#print()

#p = r'\d\d\d\d\d\d\d\d\d\d\d\d'
#result = re.findall(p, s)
#print(result)
#print()

#p = r'\d{12}'
#result = re.findall(p, s)
#print(result)
#print()

#p = r'\+\d{12}'
#result = re.findall(p, s)
#print(result)
#print()

#p = r'\d+'
#result = re.findall(p, s)
#print(result)
#print()

#p = '\w+'
#result = re.findall(p, s)
#print(result)
#print()


#s = '''Mobile number: (91) 9006228083'''
#p = '\(\d{2}\) \d+'
#result = re.findall(p, s)
#print(result)
#print()



s = """Elon musk's phone number is 9991116666, call him you have any question on dodgecoin. Tesla's revenue is 40 billion. Tesla's CFO number (999)-333-7777"""

p = re.findall(r"\d",s)
print(p)

p = re.findall(r"\d\d",s)
print(p)

p = re.findall(r"\d\d\d",s)
print(p)

p = re.findall(r"\d{3}",s)
print(p)

p = re.findall(r"\d{10}",s)
print(p)

p = re.findall(r"\(\d{3}\)-\d{3}-\d{4}",s)
print(p)


import re

p = re.findall(r"\d{2}:",data)
#print(p)



s = "charlie chaplin coa and the chocolate factory"
s2 = "xyz,yz,xyzz,xyyz,xxxzzy,zyz,xxyyzz,xyzxyz"

p = re.findall(r"cha|tor",s)
print(p)

p = re.findall(r"ch?a",s)
print(p)

p = re.findall(r"xy+z",s2)
print(p)

p = re.findall(r"x{2,4}",s2)
print(p)()