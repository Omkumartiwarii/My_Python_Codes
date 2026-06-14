string = input("Enter a string : ")
char_freq = {}
for i in string:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1

for i in string:
    if char_freq[i] == 1:
        print("First non-repeating character is:", i)
        break
else:
    print("No non-repeating character found")
