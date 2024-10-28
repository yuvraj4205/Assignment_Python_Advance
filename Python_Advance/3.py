#Write a Python program to read first n lines of a file.

read=input("This is first line.")
read1=int(input("This is second line."))

file=open(read,'r')

for line1 in range(read1):
    line=file.readline()
    
    if not line: 
        break
    print(line,end='')
file.close()