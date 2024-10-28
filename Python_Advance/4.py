#Write a Python program to read last n lines of a file.

file_path='Tops2.txt'
n=2

file=open(file_path,'r')
lines=file.readlines()

start=max(0,len(lines)-n)

for line in lines[start:]:
    print(line,end='')

file.close()