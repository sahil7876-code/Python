# count frequency of each name store t in disctionary and display it
cnt = 0
d = {}
with open('stud-2.txt', 'r')as f:
    for i in f:
        i = i.strip()
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

print(d)