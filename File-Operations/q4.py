# Count the number of line in a file

with open('demo.txt', 'r') as f:
    print(len(f.readlines()))