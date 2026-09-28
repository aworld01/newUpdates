'''
01. Create a Student class with basic data and a method.
    Attributes: name, age, grade
    
    Use __init__(self, name, age, grade) to set them.


02. Add method:
    Method name: info
    It should print: "Student: <name>, Age: <age>, Grade: <grade>"
    
03. Test
    Create 2 students:
    	Student("Abdul",22,"A")
    	Student("Ali",20,"B")
'''
class Student:
	def __init__(self,name,age,grade):
		self.name = name
		self.age = age
		self.grade = grade
		
	def info(self):
		print(f'Student: {self.name} Age: {self.age} Grade: {self.grade}')
		
abdul = Student("Abdul",22,"A")
ali = Student("Ali",20,"B")
abdul.info()
ali.info()