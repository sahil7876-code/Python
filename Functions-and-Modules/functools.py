from functools import reduce
l=[2,3,4,5,6]

def add(a,b):
    return a+b

print(reduce(add, l, 20))