# Write names longer than 5 char into new file

with open('student.txt', 'r') as f:
    with open('new_stud.txt', 'w') as w:
        for i in f:
            i = i.strip()
            if len(i) > 5:
                w.write(i + '\n')