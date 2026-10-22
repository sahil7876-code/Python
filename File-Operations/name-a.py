# print names containing a in it

with open('student.txt','r') as f:
    for i in f:
        if 'a' in i:
            print(i)