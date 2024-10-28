#Write a Python program to count the number of lines in a text file.

file_name='Tops2.txt'

line1=0
with open(file_name,'r') as file: 
    for line in file:
        line1=line1+1

print("Number of lines:",line1)