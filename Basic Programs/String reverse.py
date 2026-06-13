string = input("Enter a string: ")
reversed_string = string[::-1]

print("Reversed string:", reversed_string)

#another method
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)