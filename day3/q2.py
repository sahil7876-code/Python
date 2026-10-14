# Read  all the lines. Print total no. of lines and display 2nd & 4th lines

with open('files/q2.txt', 'r') as f:
    lines = f.readlines()
    print("Total no. of lins in content:",len(lines))
    print("\nPrinting 2nd and 4th Line:")
    print(lines[1], end="")
    print(lines[3], end="")
