import glob

files = glob.glob("*")
print(files)
print()

file=(files[0])
print(file)
print()

name,_=file.split(".")
print(name)
print()

newName = name+"_hindi.py"
print(newName)