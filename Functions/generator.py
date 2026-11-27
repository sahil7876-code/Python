# x = (i**2 for i in range(10))
# for _ in x:
    # print(_)
# print(x)

# a = x
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# for _ in a:
#     print(_)

# def func():
#     for i in range(10):
#         c = i*2
#         yield c

# b = func()
# for i in b:
#     print(i)


# def rev(a):
#     for i in range(a, 0 , -1):
#         yield i

# x = rev(10)
# for _ in x:
#     print(_)

# def func():
#     for i in range(10):
#         c = i*3
#         yield c

# b = func()
# for i in b:
#     print(i)



# def func(n):
#     for i in range(11):
#         c = n, "*", i, "=", n*i
#         yield c

# t = func(8)
# for _ in t:
#     print(_)

l=[2,4,-3,21,-5,76,-93,3,556,-6]

def pos():
    for i in l:
        if i == abs(i):
            yield i

p = pos()
for i in p:
    print(i)