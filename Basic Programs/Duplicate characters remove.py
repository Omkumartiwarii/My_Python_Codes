#Approach 1: Loop + Set Approach
word = input("Enter a string: ")

result = ""
seen = set()

for ch in word:
    if ch not in seen:
        result += ch
        seen.add(ch)

print(result)


