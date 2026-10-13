# Print the multiplication table for odd numbrers from 1 to 10

for i in range(1, 11):
    if i % 2 != 0:
        print("\nTable of ", i,)
        for j in range(1, 11):
            print(i, "*", j, "=", i * j)