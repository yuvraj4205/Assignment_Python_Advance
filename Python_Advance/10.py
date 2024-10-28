#Write a Python program to write a list to a file.

items=["apple", "banana", "cherry", "date", "elderberry"]
file=open("fruits.txt","w")

for item in items:
    file.write(item+"\n")
file.close()

file=open("fruits.txt","r")
print(file.read())
file.close()