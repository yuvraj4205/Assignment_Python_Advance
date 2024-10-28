#Write a Python program to read a file line by line and store it into a list

file='Tops2.txt'
list=[]

file=open(file,'r')

for line in file:
    list.append(line.strip())

file.close()
print(list)