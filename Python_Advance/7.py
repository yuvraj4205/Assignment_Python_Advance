#Write a python program to find the longest words.

words=["apple", "banana", "cherry", "date", "elderberry","fig", "grape", "honeydew", "kiwi", "lemon",
       "mango", "nectarine", "orange", "papaya", "quince","raspberry", "strawberry", "tangerine", "watermelon"]

length=0
longest_words=[]

for word in words:
    if len(word)>length:
        length=len(word)
        longest_words=[word]
    elif len(word)==length:
        longest_words.append(word)
        
print("Longest words:",longest_words)
print("Length of longest words:",length)