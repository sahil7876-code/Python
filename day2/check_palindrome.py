# Check if a number is a Palindrome or not

name =input("Enter a name: ")
rev = name[::-1]

if name == rev:
    print("Palindrome")
else:
    print("Not Palindrome")