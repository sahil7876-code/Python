# read the file move the pointer to the beginning and agsin read the file

with open('demo.txt', 'r') as f:
    print(f.read())

    f.seek(0)

    print('againn\n', f.read())