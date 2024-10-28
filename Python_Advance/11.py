#Write a Python program to copy the contents of a file to another file.

File1='Tops2.txt'
File2='copy.txt'

file3=open(File1, 'r')

content=file3.read()

file4=open(File2,'w')

file4.write(content)

file3.close()
file4.close()

print("Contents copied from",File1,"to",File2)