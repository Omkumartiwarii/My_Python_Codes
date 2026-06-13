#Word count in String

#Approach 1: Using Built-in Functions
word = input("Enter a string: ")
word_list = word.split()
word_count = len(word_list)
print(f"Number of words in the string: {word_count}")


#Approach 2: Using Loop
word = input("Enter a string: ")
word_list = word.split()
word_count = 0
for i in word_list:
    word_count += 1
print(f"Number of words in the string: {word_count}")