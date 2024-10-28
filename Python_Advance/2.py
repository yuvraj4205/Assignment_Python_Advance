#Write a Python program to append text to a file and display the text.

File=open("Tops1.txt","w")
File.write("This is file management demo using Python.")
File.close()
print("File Written Successfully.")
print("****************************************************")

File=open("Tops1.txt","a")
File.write("\nThis file is now appended.")
File.close()
print("File Appended Successfully.")
print("****************************************************")

File=open("Tops1.txt","r")
print(File.read())
File.close()
print("****************************************************")