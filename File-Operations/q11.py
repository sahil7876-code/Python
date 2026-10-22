# copy content from one to another file

with open('demo.txt', 'r') as f:
    data = f.read()

with open('demo2.txt', 'w') as fe:
    fe.write(data)