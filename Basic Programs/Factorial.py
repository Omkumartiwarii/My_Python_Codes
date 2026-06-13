num = int(input("Enter a number: "))
sum = 1
for i in range(1, num + 1):
    sum *= num
    num -= 1
print(f"Factorial of {num} is {sum}")