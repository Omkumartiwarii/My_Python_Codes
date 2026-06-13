#approach 1: Using Built-in Functions
word = input("Enter a string: ")
print(f"Uppercase: {word.upper()}")
print(f"Lowercase: {word.lower()}")


#approach 2: Using Loop
word = input("Enter a string: ")
uppercase = ""
lowercase = ""
for char in word:
    if char.isupper():
        uppercase += char
    elif char.islower():
        lowercase += char
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")