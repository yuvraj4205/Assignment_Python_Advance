#Write a Python program to count the frequency of words in a file.

file_name='Tops1.txt'
word1={}

with open(file_name,'r') as file:
  for line in file:
    words = line.lower().split()
    for word in words:
      if word in word1:
        word1[word]+=1
      else:
        word1[word]=1

print("Word Counts:")
for word, count in word1.items():
  print(word,":",count)