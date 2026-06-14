#Approach 1: Loop + Set Approach
word = input("Enter a string: ")

result = ""
seen = set()

for ch in word:
    if ch not in seen:
        result += ch
        seen.add(ch)

print(result)


#Approach 2: Using Dictionary
word = input("Enter a string: ")

char_freq = {}

for ch in word:
    if ch not in char_freq:
        char_freq[ch] = 1

print("".join(char_freq.keys()))


#Approach 3: Using Set
word = input("Enter a string : ")
print("".join(set(word)))


#Approach 4: dict.fromkeys() One-Liner
word = input("Enter a string : ")

print("".join(dict.fromkeys(word)))