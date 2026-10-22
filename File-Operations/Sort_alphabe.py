# Sort students names in aplphabetically order

l = []
with open('student.txt', 'r') as f:
    for i in f:
        i = i.strip()
        l.append(i)
l.sort()
print(l)