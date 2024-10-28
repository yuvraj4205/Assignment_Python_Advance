#Write python program that user to enter only odd numbers, else will raise an exception.

number=int(input("Please enter an odd number: "))

if number%2==0:
    print("Please enter an odd number.")
else:
    print("Your entered number is odd.")