#addition of multiple args

n1 = int(input('Enter how many num'))
n = []
for i in range(n1):
    num = int(input("Enter number"))
    n.append(num)

def add(*args):
    l = 0
    for i in args:
        l += i

    return l
    
print(add(*n))


def info(**details):
    print(details['name'])

info(name='sujal', city='pune')


#wap to display name, company, total salary of 5 months using args and kwargs

def info(*salary, **detail):
    print(detail['name'])
    print(detail['company'])
    ts = 0
    for i in salary:
        ts += i
    print(ts)

info(10000, 20000, 30000, 40000, 50000, name = 'Sahil', company='Amazon' )


a = 0
def func(n = 10):
    temp = 10
    global a 
    a += 10
    def sum():
        global a 
        a += 10
        return temp + n
    return sum()
    
print(func())
print(a)









for i in range(1, 5+1):
    for j in range(i): 
        print("*", end="")
    for j in range(2*(5-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

for i in range(5-1, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2*(5-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()