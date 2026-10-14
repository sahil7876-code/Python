# Read a file, split it into words, store them and 
# 1. Print total no. of words
# 2. Print all unique words

with open('files/q4.txt', 'r') as f:
    cont = f.read().lower()
    #print(cont)
    cont1 = cont.split()
print("Total words: ",len(cont1))
unique = set(cont1)
#text = unique.lower()
print("Unique words: ",unique)