# Print names longer than 5 chars

with open('student.txt', 'r') as f:
    for i in f:
        i = i.strip()
        if len(i) > 5:
            print(i)