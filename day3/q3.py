# Take a sentence from user, split it into words, store them in a list. Print the largest word from it

sent = input("Enter a sentence: ")
words = sent.split()

large = ""
for i in words:
    if len(i) > len(large):
        large = i

print(large)