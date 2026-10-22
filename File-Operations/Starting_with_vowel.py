# Count names starting with vowels

cnt = 0
v='aeiouAEIOU'
with open('student.txt', 'r') as f:
    for i in f:
        i = i.strip()
        if i[0] in v:
            cnt += 1
    print(cnt)