#Write a Python program to read a file line by line store it into a variable.

file='Tops2.txt'
lines=[]

file=open(file,'r')

for line in file:
    lines.append(line.strip())
    
file.close()
for line in lines:
    print(line)