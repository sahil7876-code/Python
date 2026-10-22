# Read the and retur the current pos and read same file from a saved pointer position

with open('demo.txt', 'r') as f:
    print(f.read(6))

    pos = f.tell()

    print(f.seek(pos))
    print(f.read())