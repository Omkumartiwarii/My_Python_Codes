char = input("Enter a string: ")
char_freq = {}
for i in char:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1