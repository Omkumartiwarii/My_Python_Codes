string = input("Enter a string: ")

words = string.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest word: {longest_word}")
print(f"Length of longest word: {len(longest_word)}")
