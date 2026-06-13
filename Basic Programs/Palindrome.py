#Approach 1: Using String Slicing

num = input("Enter a number to check palindrome: ")
reversed_number = num[::-1]
if num == reversed_number:
    print(f"{num} is palindrome number")
else :
    print(f"{num} is not palindrome number")
    
    
#Approach 2: Using Loop

num = int(input("Enter a Number: "))

original_num = num
new_num = 0

while num != 0:
    remainder = num % 10
    new_num = new_num * 10 + remainder
    num //= 10

if original_num == new_num:
    print(f"{original_num} is a palindrome number")
else:
    print(f"{original_num} is not a palindrome number")