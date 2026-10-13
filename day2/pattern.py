# print the following pattern
#-*
#-##
#-***

n = int(input ("Enter the size: "))
for i in range(1, n):
    if i % 2 == 0:
        print("*"*i)
    else:
        print("#"*i)