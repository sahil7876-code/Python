
print(max(2,3,4,5))

l = [4,22,-7,99,-3,1]
print(min(l))


l = [4,22,-7,99,-3,1]
l1 = []
for i in l:
    if i < 0:
        l1.append(abs(i))
    else:
        l1.append(i)

print(l1)