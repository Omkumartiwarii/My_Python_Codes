string = input("Enter a string: ")

words = string.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest word: {longest_word}")
print(f"Length of longest word: {len(longest_word)}")



#Approach 2: Using Built-in Function (max() with key=len)
string = input("Enter a string: ")
words = string.split()
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")
print(f"Length of longest word: {len(longest_word)}")