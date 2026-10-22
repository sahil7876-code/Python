# read the file and store students name from the file into list

list = []
with open('student.txt', 'r') as f:
    #data = f.readlines()
    #list.append(data)
    #print(list)

    for i in f:
        list.append(i)
    print(list)