# Write a program to read a file and count how many vowels are present in it's content

with open("files/demo.txt", 'r') as f:
    read = f.read()

count = 0
for c in read:
    if c in 'aeiouAEIOU':
        count += 1

print("Vowels in files:",count)