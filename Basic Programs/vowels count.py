#Vowels count in String
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string: #char is a variable that takes each character of the string one by one in each iteration of the loop
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")


#Approach 2: Using Built-in Functions
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print(f"Number of vowels in the string: {count}")