#Write a Python program to read an entire text file.

File=open("Tops1.txt","w")
File.write("This is file management demo using Python.")
File.close()
print("File Written Successfully.")
print("****************************************************")

File=open("Tops1.txt","r")
print(File.read())
File.close()
print("****************************************************")