# Find the total of the number given in the 'n'
n=int(input("Enter a number: "))
num = str(n)
total = 0
if n < 0:
    print("Please enter a positive number")
else:
    for i in num:
        total += int(i)

print("Sum: ", total)