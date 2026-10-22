# read file from the beginning after reaching at the end of the file

with open('demo.txt','r') as f:
    print(f.read())

    f.seek(0)

    print(f.read())