'''
Read student names from student.txt and, for each name, display:
1. The name
2. Its length
3. Its first character
4. Its last character
5. Whether it is a palindrome
'''

with open('student.txt', 'r') as f:
    for i in f:
        i = i.strip()
        print('Name:',i)
        print('Length:',len(i))
        print('First char:',i[0])
        print('Last char:',i[-1])
        if i == i[::-1]:
            print('Is Palindrome')
        else:
            print('Not Palindrome')
        print('\n')